{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMKQ9qlKUph1yBwBZz1GBiA"
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
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "BJozhxWD0DS6",
        "outputId": "b13c2184-a322-4c8d-c69c-cca71db9210f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Python Puro\n",
            "Lista vezes 2: [100000, 200000, 300000, 100000, 200000, 300000]\n",
            "\n",
            "Solução NUMPY\n",
            "Array vezes 2: [200000 400000 600000]\n",
            "[[1 2 3]\n",
            " [4 5 6]]\n"
          ]
        }
      ],
      "source": [
        "import numpy as np #as = alias | chame a lib \"numpy\" como \"np\"\n",
        "\n",
        "print(\"Python Puro\")\n",
        "precos_lista = [100_000, 200_000, 300_000]\n",
        "\n",
        "print(\"Lista vezes 2:\", precos_lista * 2)\n",
        "\n",
        "print(\"\\nSolução NUMPY\")\n",
        "precos_numpy = np.array([100_000, 200_000, 300_000])\n",
        "\n",
        "precos_atualizados = precos_numpy * 2\n",
        "print(\"Array vezes 2:\", precos_atualizados)\n",
        "\n",
        "matriz_dados = np.array([\n",
        "  [1, 2, 3],\n",
        "  [4, 5, 6]\n",
        "])\n",
        "\n",
        "print(matriz_dados)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Operações Matemáticas e Estatíscas com NumPy\n",
        "dados = np.array([10, 20, 30, 40, 50])\n",
        "\n",
        "print(\"Soma de todos os elementos:\", dados.sum())\n",
        "print(\"Média aritmética:\", dados.mean())\n",
        "print(\"Desvio padrão:\", dados.std().round(2))\n",
        "print(\"Valor mínimo:\", dados.min())\n",
        "print(\"Valor máximo:\", dados.max())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "MQRkwH6T35_M",
        "outputId": "51f371e2-1397-4780-d053-bb0521a9f274"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Soma de todos os elementos: 150\n",
            "Média aritmética: 30.0\n",
            "Desvio padrão: 14.14\n",
            "Valor mínimo: 10\n",
            "Valor máximo: 50\n"
          ]
        }
      ]
    }
  ]
}