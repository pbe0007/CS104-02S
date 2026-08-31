{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyPxQ3wBmCJza9FOo0cgCFLa",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/pbe0007/CS104-02S/blob/main/Cs104_general.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 8 / 31  Lecture"
      ],
      "metadata": {
        "id": "gpjvyYOBZSDc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#boolean type\n",
        "age = int(input(\"How old are you? \"))\n",
        "senior = age >= 65\n",
        "print(senior)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n-BK9HtEZSmM",
        "outputId": "cbb5e5f7-d97c-4926-ea1f-77df22b688f5"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "How old are you?66\n",
            "True\n",
            "c\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#score grader\n",
        "grade = int(input(\"input score \"))\n",
        "letter_grade = \"error\"\n",
        "if grade >= 90:\n",
        "  letter_grade = \"A\"\n",
        "elif grade >= 80:\n",
        "  letter_grade = \"B\"\n",
        "elif grade >= 70:\n",
        "  letter_grade = \"C\"\n",
        "elif grade >= 60:\n",
        "  letter_grade = \"D\"\n",
        "else:\n",
        "  letter_grade = \"F\"\n",
        "print(\"letter grade: \"+ letter_grade)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0len_4K7c6YM",
        "outputId": "70ce448e-5c3c-4203-fe8e-a204e298d9f4"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "input score 7\n",
            "letter grade: F\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#while loop version\n",
        "count = 0\n",
        "sum = 0\n",
        "\n",
        "def check_int(x):\n",
        "  try:\n",
        "    int(x)\n",
        "    return(True)\n",
        "  except:\n",
        "    return(False)\n",
        "\n",
        "while count < 2:\n",
        "  grade = input(\"input score \")\n",
        "  letter_grade = \"error\"\n",
        "  if check_int(grade) == False:\n",
        "    print(\"please only input numbers\")\n",
        "    continue\n",
        "  elif int(grade) <= 0:\n",
        "    print(\"no negative numbers\")\n",
        "    continue\n",
        "  elif int(grade) >= 90:\n",
        "    letter_grade = \"A\"\n",
        "    count+=1\n",
        "  elif int(grade) >= 80:\n",
        "    letter_grade = \"B\"\n",
        "    count+=1\n",
        "  elif int(grade) >= 70:\n",
        "    letter_grade = \"C\"\n",
        "    count+=1\n",
        "  elif int(grade) >= 60:\n",
        "    letter_grade = \"D\"\n",
        "    count+=1\n",
        "  else:\n",
        "    letter_grade = \"F\"\n",
        "    count+=1\n",
        "  sum += int(grade)\n",
        "  print(\"letter grade: \"+ letter_grade)\n",
        "\n",
        "average = sum/count\n",
        "\n",
        "print(\"The average is: \" + str(average))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "id": "KuJN1EGafR0q",
        "outputId": "02374316-b1df-4b16-9652-b421a5892e5b"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "input score t\n",
            "please only input numbers\n",
            "input score 66\n",
            "letter grade: D\n",
            "input score 80\n",
            "letter grade: B\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "can only concatenate str (not \"float\") to str",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_5754/2071749921.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     39\u001b[0m \u001b[0maverage\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msum\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0mcount\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     40\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 41\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"The average is: \"\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0maverage\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     42\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: can only concatenate str (not \"float\") to str"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#other if statement fun\n",
        "a = input(\"Boo! \")\n",
        "a = a.lower()\n",
        "if a[:3] == \"ahh\":\n",
        "  print(\"gotcha\")\n",
        "elif a[:4] == \"what\":\n",
        "  print(\"aww\")\n",
        "else:\n",
        "  print(\"what?\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NMVZ3PQUbojJ",
        "outputId": "3d2aa60c-6510-49ba-c2fc-b88de4b78dba"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Boo! huh?\n",
            "what?\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#this was on the board\n",
        "a = \"C\"\n",
        "a = a.lower()\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FDeAenjSaw3X",
        "outputId": "f9c5b15d-e3c1-419f-fc5b-218afd500153"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "c\n"
          ]
        }
      ]
    }
  ]
}