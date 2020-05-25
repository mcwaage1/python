{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the substance's temperature in Celsius: 14\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The temperature is acceptable.\n",
      "Check it again in 15 minutes.\n"
     ]
    }
   ],
   "source": [
    "# A scenario where a lab tech needs to check the temperatue of a substance \n",
    "# and make sure it doesn't go above a certain temperature\n",
    "\n",
    "max_temp = 102.5\n",
    "\n",
    "temperature = float(input(\"Enter the substance's temperature in Celsius:\"))\n",
    "while temperature > max_temp:\n",
    "    print(\"The temperature is too high.\")\n",
    "    print(\"The the thermostat down and wait 5 minutes.\")\n",
    "    print(\"Then take the temperature again and enter it.\")\n",
    "    temperature = float(input(\"Enter the new temperature in Celsius:\"))\n",
    "\n",
    "print(\"The temperature is acceptable.\")\n",
    "print(\"Check it again in 15 minutes.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
