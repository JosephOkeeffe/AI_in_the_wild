#ifndef PROTECT_H
#define PROTECT_H

#include "Droid.h"
#include "Routine.h"
#include <iostream>
#include <cmath>

class Protect : public Routine
{
public:

    int destX;
    int destY;
    sf::Vector2f target;
    int droidA;
    int droidB;

    Protect(int droidA, int droidB, Grid& g) : Routine()

    {
        this->destX = 1;
        this->destY = 1;
        this->target = g.getGridLocation(destX, destY);
        this->routineType = "Protect";
        this->routineGrid = &g;

        this->droidA = droidA;
        this->droidB = droidB;


        if (droidA != -1)
        {
            this->droidA = droidA - 1;
        }
        if (droidB != -1)
        {
            this->droidB = droidB - 1;
        }
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

            sf::Vector2f protectPoint = MoveToClosestProtectPoint(grid);
            destX = round(protectPoint.x);
            destY = round(protectPoint.y);

            destX = std::clamp(destX, 1, grid.gridSize);
            destY = std::clamp(destY, 1, grid.gridSize);

            droid->target = grid.getGridLocation(destX, destY);

            if (!isDroidAtDestination(droid, grid)) 
            {
                moveDroid(droid, grid);
            }
            else 
            {
                succeed("Protect for " + droid->name);
            }
        }
    }

    sf::Vector2f MoveToClosestProtectPoint(Grid& grid)
    {
        int droidAx = grid.m_gridDroids[droidA]->x;
        int droidAy = grid.m_gridDroids[droidA]->y;
        int droidBx = grid.m_gridDroids[droidB]->x;
        int droidBy = grid.m_gridDroids[droidB]->y;

        return sf::Vector2f((droidAx + droidBx) / 2.0f, (droidAy + droidBy) / 2.0f);
    }

    void moveDroid(Droid* droid, Grid& grid)
    {
        std::cout << ">>> Droid " << droid->name << " moving to " << destX << ", " << destY << std::endl;

        if (destX < 1 || destX > grid.gridSize || destY < 1 || destY > grid.gridSize)
        {
            return;
        }

        sf::Vector2f direction = droid->target - droid->position;

        if (std::abs(grid.length(direction)) > 0)
        {
            if (droid->target.y != droid->position.y)
            {
                if (droid->target.y > droid->position.y)
                {
                    droid->position.y = droid->position.y + 1;
                }
                else 
                {
                    droid->position.y = droid->position.y - 1;
                }
            }
            if (droid->target.x != droid->position.x)
            {
                if (droid->target.x > droid->position.x)
                {
                    droid->position.x = droid->position.x + 1;
                }
                else 
                {
                    droid->position.x = droid->position.x - 1;
                }
            }
        }

        if (isDroidAtDestination(droid, grid)) 
        {
            succeed("MoveTo for " + droid->name);
        }
    }

    bool isDroidAtDestination(Droid* droid, Grid& grid)
    {
        sf::Vector2f direction = droid->target - droid->position;
        return ((int)grid.length(direction) == 0);
    }
};

#endif
