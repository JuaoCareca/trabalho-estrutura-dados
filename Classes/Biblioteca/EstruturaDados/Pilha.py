# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Basic example of an adapter class to provide a stack interface to Python's list."""

# -*- coding: utf-8 -*-

# from ..exceptions import Empty
# import from exceptions

class Empty(Exception):
    def __init__(self, valor):
      self.valor = valor

    def __str__(self):
      return repr(self.valor)

class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      #raise Empty('Stack is empty')
      print('pilha vazia')
      return None
    else:
      return self._data[-1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      # raise Empty('Stack is empty')
      print('pilha vazia')
      return None
    else:
      return self._data.pop()               # remove last item from list
  
  def criar_copia(self):
    # Criar uma pilha auxiliar
    aux = ArrayStack()

    # Pegar todos os dados dessa pilha e colocar no aux
    while not (self.is_empty()):
        
      # O aux ficará com os dados inversos
      aux.push(self.pop())
    
    # Como o aux ficará inverso, ele será passado para a copia e para a classe
      
    # Criar pilha cópia
    copia = ArrayStack()

    while  not (aux.is_empty()):
       
      # Guardar o retirado numa variável
      retirado = aux.pop()

      # Colocar o dado retirado na copia e original
      copia.push(retirado)
      self.push(retirado)
    
    # Por fim, Retornar a copia
    return copia
    

if __name__ == '__main__':

    def printStack(s):
        copia = ArrayStack() # instaciou pilha auxiliar
        print('[', end="")
        while(not s.is_empty()): # enquanto a pilha s nao ficar vazia
            print(s.top(), end=" ") # exibe o elemento do topo da pilha
            copia.push(s.pop()) # adicionar o elem do topo na pilha auxiliar e desempilhar
        while(not copia.is_empty()):
            s.push(copia.pop())
        copia = None
        print(']\n')




    S = ArrayStack()                 # contents: [ ]
    printStack(S)
    print(S.top())
    S.push(5)                        # contents: [5]
    printStack(S)
    S.push(3)                        # contents: [5, 3]
    printStack(S)
    print(len(S))                    # contents: [5, 3];    outputs 2
    print(S.pop())                   # contents: [5];       outputs 3
    printStack(S)
    print(S.is_empty())              # contents: [5];       outputs False
    print(S.pop())                   # contents: [ ];       outputs 5
    printStack(S)
    print(S.pop())  # contents: [ ];       outputs 5
    printStack(S)
    print(S.is_empty())              # contents: [ ];       outputs True
    S.push(7)                        # contents: [7]
    printStack(S)
    S.push(9)                        # contents: [7, 9]
    printStack(S)
    print(S.top())                   # contents: [7, 9];    outputs 9
    printStack(S)
    S.push(4)                        # contents: [7, 9, 4]
    printStack(S)
    print(len(S))                    # contents: [7, 9, 4]; outputs 3
    print(S.pop())                   # contents: [7, 9];    outputs 4
    S.push(6)                        # contents: [7, 9, 6]
    printStack(S)
    S.push(8)                        # contents: [7, 9, 6, 8]
    printStack(S)
    print(S.pop())                   # contents: [7, 9, 6]; outputs 8
    printStack(S)
