{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "105e4da7-fcec-47db-a200-8033be41b1b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Eligible to vote\n"
     ]
    }
   ],
   "source": [
    "age = 25\n",
    "if age >= 18:\n",
    "    print(\"Eligible to vote\")\n",
    "else:\n",
    "    print(\"Not eligible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f1f92ef0-94a0-4b10-a485-d2366efb8d5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Not eligible\n"
     ]
    }
   ],
   "source": [
    "age = 16\n",
    "if age >= 18:\n",
    "    print(\"Eligible to vote\")\n",
    "else:\n",
    "    print(\"Not eligible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "56a7b125-4727-4321-ba4f-32529b20327e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Grade B\n"
     ]
    }
   ],
   "source": [
    "marks = 85\n",
    "if marks >= 90:\n",
    "    print(\"Grade A\")\n",
    "elif marks >= 75:\n",
    "    print(\"Grade B\")\n",
    "elif marks >= 60:\n",
    "    print(\"Grade C\")\n",
    "else:\n",
    "    print(\"Grade D\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2ffed0d6-7aed-40b5-b1d4-2bdf4a165f37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Grade D\n"
     ]
    }
   ],
   "source": [
    "marks = 50\n",
    "if marks >= 90:\n",
    "    print(\"Grade A\")\n",
    "elif marks >= 75:\n",
    "    print(\"Grade B\")\n",
    "elif marks >= 60:\n",
    "    print(\"Grade C\")\n",
    "else:\n",
    "    print(\"Grade D\")   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "025cec60-1774-4909-bd1a-0736cb677967",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number is odd\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter number\"))\n",
    "if num %2== 0:\n",
    "    print(\"Number is even\")\n",
    "else:\n",
    "    print(\"Number is odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "33042df5-8fd1-48c3-a3fc-318497e050b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number a 43\n",
      "Enter number b 54\n",
      "Enter number c 23\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b is greater\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"Enter number a\"))\n",
    "b = int(input(\"Enter number b\"))\n",
    "c = int(input(\"Enter number c\"))\n",
    "if a > b:\n",
    "    print(\"a is greater\")\n",
    "if b > c:\n",
    "    print(\"b is greater\")\n",
    "else:\n",
    "    print(\"c is greater\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2e1f9c8e-d5e2-47bc-90f4-48125c795061",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Eligible for vote\n"
     ]
    }
   ],
   "source": [
    "age = 25\n",
    "citizen = True\n",
    "if age >= 18:\n",
    "  if citizen:\n",
    "    print(\"Eligible for vote\")\n",
    "else:\n",
    "    print(\"No eligible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "239bcb02-5051-4910-b4c7-123cec53d91c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No eligible\n"
     ]
    }
   ],
   "source": [
    "age = 17\n",
    "citizen = True\n",
    "if age >= 18:\n",
    "  if citizen:\n",
    "    print(\"Eligible for vote\")\n",
    "else:\n",
    "    print(\"No eligible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "cbae14bd-309f-4521-9996-95f9351b515a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Working age\n"
     ]
    }
   ],
   "source": [
    "age = 25\n",
    "if age >= 18 and age <= 65:\n",
    "    print(\"Working age\")\n",
    "else:\n",
    "    print(\"Not working age\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "fd617d8c-9e84-470f-bdf4-81f0b0d918c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Eligible for gracing marks\n"
     ]
    }
   ],
   "source": [
    "marks = 35\n",
    "if marks >= 40 or marks == 35:\n",
    "    print(\"Eligible for gracing marks\")\n",
    "else:\n",
    "    print(\"Not eligible for gracing marks\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "0e9a9b12-7c05-410d-87f1-2b6f66c4f0d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Don't go to office\n"
     ]
    }
   ],
   "source": [
    "is_holiday = False\n",
    "if not is_holiday:\n",
    "    print(\"Don't go to office\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "ed30ad16-bb91-43c1-b5fc-43cf37f7373c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "adult\n"
     ]
    }
   ],
   "source": [
    "age = 25\n",
    "status = \"adult\" if age >= 18 else \"minor\"\n",
    "print(status)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "faf30120-c73d-4cd8-9ca6-b3df453172b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter year 2020\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Leap year\n"
     ]
    }
   ],
   "source": [
    "year = int(input(\"Enter year\"))\n",
    "status = \"Leap year\" if year%4==0 else \"Not leap year\"\n",
    "print(status)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2da680df-8aba-4ce1-92da-e504df3276a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Eligible for promotion\n"
     ]
    }
   ],
   "source": [
    "salary = 60000\n",
    "experience = 4\n",
    "if salary >= 50000 and experience >= 3:\n",
    "    print(\"Eligible for promotion\")\n",
    "else:\n",
    "    print(\"Not eligible\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f895abd9-7435-4918-8405-d535c58bce1b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
