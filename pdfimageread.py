{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Welcome To Colaboratory",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true,
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
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
        "<a href=\"https://colab.research.google.com/github/nvlatha/Azurewebapp/blob/master/pdfimageread.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5TV2viy0eQg9",
        "outputId": "82dc9d4f-c38f-44cc-805b-a72b102f131b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "! pip install pytesseract"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting pytesseract\n",
            "  Downloading pytesseract-0.3.8.tar.gz (14 kB)\n",
            "Requirement already satisfied: Pillow in /usr/local/lib/python3.7/dist-packages (from pytesseract) (7.1.2)\n",
            "Building wheels for collected packages: pytesseract\n",
            "  Building wheel for pytesseract (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pytesseract: filename=pytesseract-0.3.8-py2.py3-none-any.whl size=14072 sha256=88299836d481305218d02e06fd4792eccc9112c7c2466707b36c1485b8794068\n",
            "  Stored in directory: /root/.cache/pip/wheels/a4/89/b9/3f11250225d0f90e5454fcc30fd1b7208db226850715aa9ace\n",
            "Successfully built pytesseract\n",
            "Installing collected packages: pytesseract\n",
            "Successfully installed pytesseract-0.3.8\n"
          ]
        }
      ]
    }
  ]
}