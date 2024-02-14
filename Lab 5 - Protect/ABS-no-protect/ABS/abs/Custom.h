#include "Droid.h"
#include "MoveTo.h"
#include <iostream>
#include <vector>
#include <SFML/Graphics.hpp>

class Custom : public Routine {

public:

    MoveTo* moveTo;
    std::vector<std::pair<int, int>> customPoints;
    int currentPointIndex;
    sf::Clock rotationClock;
    bool rotationInProgress;

    Custom(Grid& grid) : Routine(), currentPointIndex(0), rotationInProgress(false)
    {
        customPoints = { {15, 3}, {3, 10}, {3, 20}, {15, 26}, {26, 20}, {26, 10} };
        moveTo = new MoveTo(customPoints[0].first, customPoints[0].second, grid);
        this->routineType = "MoveToSpecificPoints";
        this->routineGrid = &grid;
    }

    void start(string msg)
    {
        std::cout << ">>> Starting routine " << routineType << msg << std::endl;
        state = RoutineState::Running;
        moveTo->start(" to a specific point.");
    }

    void reset(string msg)
    {
        std::cout << ">>> Resetting routine " << routineType << msg << std::endl;
        currentPointIndex = 0;
        moveTo = new MoveTo(customPoints[currentPointIndex].first, customPoints[currentPointIndex].second, *routineGrid);
        rotationInProgress = false;

        moveTo->reset(" to a specific point");
        state = RoutineState::None;
    }

    void act(Droid* droid, Grid& grid)
    {
        if (rotationInProgress)
        {
            rotateDroid(droid);
            return;
        }

        if (!moveTo->isRunning())
        {
            if (rotationInProgress)
            {
                rotateDroid(droid);
            }
            else
            {
                moveToNextPoint();
            }
        }

        moveTo->act(droid, grid);

        if (moveTo->isSuccess())
        {
            std::cout << "Reached destination. Starting rotation." << std::endl;
            startRotation();
        }
        else if (moveTo->isFailure())
        {
            fail();
        }
    }

private:
    void moveToNextPoint()
    {
        Node* currentNode = &routineGrid->nodes[customPoints[currentPointIndex].first][customPoints[currentPointIndex].second];
        currentNode->setColor(sf::Color::Red);
        currentPointIndex = (currentPointIndex + 1) % customPoints.size();
        moveTo = new MoveTo(customPoints[currentPointIndex].first, customPoints[currentPointIndex].second, *routineGrid);


        moveTo->start(" to a specific point");
    }

    void startRotation()
    {
        rotationInProgress = true;
        rotationClock.restart();
    }

    void rotateDroid(Droid* droid)
    {
        float rotationDuration = 1.0f; 
        float rotationAngle = 360.0f * (rotationClock.getElapsedTime().asSeconds() / rotationDuration);
        droid->droidSprite.rotate(rotationAngle);

        if (rotationClock.getElapsedTime().asSeconds() >= rotationDuration)
        {
            rotationInProgress = false;
            rotationClock.restart();
            std::cout << "Rotation complete. Moving to the next point." << std::endl;
            moveToNextPoint();
        }
    }


};
