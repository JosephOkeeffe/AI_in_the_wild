#ifndef PATROL_H
#define PATROL_H

#include "Droid.h"
#include "Routine.h"
#include <iostream>
#include <cmath>

class Custom : public Routine
{
public:

    sf::Vector2i patrolPointA;
    sf::Vector2i patrolPointB;
    sf::Vector2f target;

    Custom(sf::Vector2i pointA, sf::Vector2i pointB, Grid& g) : Routine(),
        patrolPointA(pointA),
        patrolPointB(pointB),
        target(g.getGridLocation(patrolPointA.x, patrolPointA.y))
    {
        this->routineType = "Patrol";
        this->routineGrid = &g;
    }

    void reset(string msg)
    {
        std::cout << ">>> Resetting routine " << routineType << msg << std::endl;
        state = RoutineState::None;
    }

    void act(Droid* droid, Grid& grid)
    {
        if (isRunning())
        {
            if (!droid->isAlive() || droid->alarmHasBeenRaised)
            {
                fail();
                return;
            }

            // Determine the next patrol point based on the current state
            sf::Vector2i nextPatrolPoint = (state == RoutineState::None || state == RoutineState::Success) ? patrolPointB : patrolPointA;
            target = grid.getGridLocation(nextPatrolPoint.x, nextPatrolPoint.y);

            if (!isDroidAtDestination(droid, grid))
            {
                moveDroid(droid, grid);
            }
            else
            {
                succeed("Patrol for " + droid->name);
            }
        }
    }

    void moveDroid(Droid* droid, Grid& grid)
    {
        std::cout << ">>> Droid " << droid->name << " patrolling to " << target.x << ", " << target.y << std::endl;

        sf::Vector2f direction = target - droid->position;
        if (std::abs(grid.length(direction)) > 0)
        {
            auto& position = droid->position;
            auto& targetPos = target;

            if (targetPos.y != position.y)
            {
                position.y += (targetPos.y > position.y) ? 1 : -1;
            }

            if (targetPos.x != position.x)
            {
                position.x += (targetPos.x > position.x) ? 1 : -1;
            }
        }

        if (isDroidAtDestination(droid, grid))
        {
            succeed("Patrol for " + droid->name);
        }
    }

    bool isDroidAtDestination(Droid* droid, Grid& grid)
    {
        sf::Vector2f direction = target - droid->position;
        return ((int)grid.length(direction) == 0);
    }
};

#endif
