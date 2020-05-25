{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#How old are you?\n",
    "age = int(input(\"How old are you (or your kid)\"))\n",
    "if age < 0:\n",
    "    print(\"You aren't even born yet!\")\n",
    "elif age == 0:\n",
    "    print(\"You were just born!\")\n",
    "elif age > 0 and age < 1:\n",
    "    print(\"You're just a baby!\")\n",
    "elif age >= 1 and age < 13:\n",
    "    print(\"You're a kid!\")\n",
    "elif age >= 13 and age < 20:\n",
    "    print(\"You're a teenager!\")\n",
    "elif age >= 20 and age < 100:\n",
    "    print(\"You're an adult now!\")\n",
    "else:\n",
    "    print(\"Are you even alive?\")"
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
