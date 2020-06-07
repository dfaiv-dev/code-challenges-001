using System;
using System.Collections.Generic;
using System.Linq;
using Xunit;

namespace HackerRank
{
    /// <summary>
    /// https://www.hackerrank.com/challenges/red-knights-shortest-path/problem
    /// </summary>
    public class RedKnightsShortestPath
    {
        // Complete the printShortestPath function below.
        static void printShortestPath(int n, int i_start, int j_start, int i_end, int j_end)
        {
            // Print the distance along with the sequence of moves.

            // move order [Name] (dx, dy) -  UL (-1,2), UR (1,2), R (2,0), LR (1,-2), LL (-1,-2), L (-2,0)

            var grid = new GridIndex(n);

            var startNode = grid.GetNode(i_start, j_start);
            startNode.Distance = 0;

            var openNodesQueue = new Queue<Node>();
            openNodesQueue.Enqueue(startNode);

            Node endNode = null;
            while (endNode == null && openNodesQueue.Any())
            {
                var activeNode = openNodesQueue.Dequeue();
                foreach (var move in Movements)
                {
                    var nextNode = grid.TryGetNode(activeNode, move);
                    if (nextNode == null) continue;
                    if (nextNode.IsVisited) continue;

                    nextNode.PreviousNode = activeNode;
                    nextNode.Distance = activeNode.Distance + 1;
                    nextNode.Move = move;
                    if (nextNode.IsPosition(i_end, j_end))
                    {
                        endNode = nextNode;
                        break;
                    }

                    openNodesQueue.Enqueue(nextNode);
                }
            }

            if (endNode == null)
            {
                Console.WriteLine("Impossible");
            }
            else
            {
                Console.WriteLine(endNode.Distance);
                var moveHistory = endNode.GetMoveHistory().Reverse()
                    .Select(m => m.Name)
                    .Aggregate((hist, mov) => $"{hist} {mov}");
                Console.WriteLine(moveHistory);
            }
        }

        /// <summary>
        /// NOTE: grid starts upper left, 0, 0, so moving up is negative
        /// </summary>
        static readonly Movement[] Movements = new[]
        {
            new Movement("UL", -2, -1),
            new Movement("UR", -2, 1),
            new Movement("R", 0, 2),
            new Movement("LR", 2, 1),
            new Movement("LL", 2, -1),
            new Movement("L", 0, -2)
        };

        class Movement
        {
            public Movement(string name, int deltaRow, int deltaCol)
            {
                Name = name;
                DeltaCol = deltaCol;
                DeltaRow = deltaRow;
            }

            public string Name { get; set; }
            public int DeltaCol { get; set; }
            public int DeltaRow { get; set; }
        }

        class Node
        {
            public Node(int row, int col)
            {
                Row = row;
                Col = col;
            }

            public int Row { get; set; }
            public int Col { get; set; }
            public int? Distance { get; set; }
            public bool IsVisited => Distance.HasValue;

            public Node PreviousNode { get; set; }
            public Movement Move { get; set; }
            public bool IsStart => PreviousNode == null;

            public bool IsPosition(int row, int col)
            {
                return Row == row && col == Col;
            }

            public IEnumerable<Movement> GetMoveHistory()
            {
                var activeNode = this;
                while (!activeNode.IsStart)
                {
                    yield return activeNode.Move;
                    activeNode = activeNode.PreviousNode;
                }
            }
        }

        class GridIndex
        {
            private readonly int _gridSize;
            // if memory is tight, use lists?. But we're probably OK.

            readonly Node[][] _grid;

            public GridIndex(int gridSize)
            {
                _gridSize = gridSize;
                _grid = new Node[gridSize][];
                for (int i = 0; i < gridSize; i++)
                {
                    var gridRow = Enumerable.Range(0, gridSize)
                        .Select(j => new Node(i, j))
                        .ToArray();

                    _grid[i] = gridRow;
                }
            }

            public Node GetNode(int i, int j)
            {
                return _grid[i][j];
            }

            public Node TryGetNode(Node sourceNode, Movement move)
            {
                var i = sourceNode.Row + move.DeltaRow;
                var j = sourceNode.Col + move.DeltaCol;
                if (i >= _gridSize || i < 0
                                   || j >= _gridSize || j < 0)
                {
                    return null;
                }

                return _grid[i][j];
            }
        }

        [Fact]
        public void SampleInput0()
        {
            /*
                7
                6 6 0 1

            4
            UL UL UL L
             */

            printShortestPath(7, 6, 6, 0, 1);
        }

        [Fact]
        public void SampleInput1()
        {
            /*
             6, 5 1 0 5
            Impossible
             */

            printShortestPath(6, 5, 1, 0, 5);
        }

        [Fact]
        public void SampleInput2()
        {
            /*
             * 7, 0 3 4 3
             *
             * 2
                LR LL
             */

            printShortestPath(7, 0, 3, 4, 3);
        }
    }
}