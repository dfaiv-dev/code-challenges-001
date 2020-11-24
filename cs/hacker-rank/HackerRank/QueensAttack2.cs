using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Xml;
using Xunit;

namespace HackerRank
{
    /// <summary>
    /// https://www.hackerrank.com/challenges/queens-attack-2/problem
    /// </summary>
    public class QueensAttack2
    {
        /// <summary>
        /// - n: an integer, the number of rows and columns in the board 
        /// - k: an integer, the number of obstacles on the board 
        /// - r_q: integer, the row number of the queen's position 
        /// - c_q: integer, the column number of the queen's position 
        /// - obstacles: a two dimensional array of integers where each element is an array of  integers, the row and column of an obstacle 
        /// </summary>
        /// <param name="n"></param>
        /// <param name="k"></param>
        /// <param name="r_q"></param>
        /// <param name="c_q"></param>
        /// <param name="obstacles"></param>
        /// <returns></returns>
        static int queensAttack(int n, int k, int r_q, int c_q, int[][] obstacles)
        {
            /*
             * Attack directions N, NE, E, SE, S, SW, W, NW
             * direction walk instruction (dx, dy):
             *     N: (0, 1), NE: (1, 1), E: (1, 0), SE: (1, -1)
             *     S: (0, -1), SW: (-1, -1), W: (-1, 0), NW: (-1, 1)
             * 
             * From queen position,
             * For each direction,
             * Walk the direction until an obstacle is hit, stop
             */


            var directions = new []
            {
                new QueenMove(0, 1),
                new QueenMove(1, 1),
                new QueenMove(1, 0),
                new QueenMove(1, -1),
                new QueenMove(0, -1),
                new QueenMove(-1, -1),
                new QueenMove(-1, 0),
                new QueenMove(-1, 1)
            };

            var obstaclesByRow = obstacles
                .GroupBy(o => o[0])
                .ToDictionary(
                    grp => grp.Key,
                    grp => new SortedSet<int>(grp.Select(obs => obs[1]).Distinct()));
            
            var obstaclesByCol = obstacles
                .GroupBy(o => o[1])
                .ToDictionary(
                    grp => grp.Key,
                    grp => new SortedSet<int>(grp.Select(obs => obs[0]).Distinct()));
            
            var queenPos = new BoardPosition(r_q, c_q);

            int validMoveCount = 0;
            foreach (var move in directions)
            {
                var rowCurrent = queenPos.Row;
                var colCurrent = queenPos.Column;

                while (true)
                {
                    rowCurrent += move.DX;
                    colCurrent += move.DY;

                    if (rowCurrent > n || colCurrent > n ||
                        rowCurrent < 1 || colCurrent < 1) break;

                    if (!obstaclesByRow.ContainsKey(rowCurrent)
                        || !obstaclesByCol.ContainsKey(colCurrent))
                    {
                        validMoveCount++;
                        continue;
                    }
                    
                    if (obstaclesByRow[rowCurrent].Contains(colCurrent)) break;

                    validMoveCount++;
                }
            }

            return validMoveCount;
        }

        public static bool HasObstacle(int row, int col, int[][] obstacles) =>
            obstacles.Any(o => o[0] == row && o[1] == col);
        
        public class QueenMove
        {
            public QueenMove(int dx, int dy)
            {
                DX = dx;
                DY = dy;
            }

            public int DX { get; set; }
            public int DY { get; set; }
        }

        public class BoardPosition
        {
            public BoardPosition(int row, int column)
            {
                Row = row;
                Column = column;
            }

            public int Row { get; set; }
            public int Column { get; set; }
        }

        [Fact]
        public void SampleInput0()
        {
            Assert.Equal(9,
                queensAttack(4, 0, 4, 4, new int[0][]));
        }

        [Fact]
        public void SampleInput1()
        {
            Assert.Equal(10,
                queensAttack(5, 3, 4, 3,
                    new[]
                    {
                        new[] {5, 5},
                        new[] {4, 2},
                        new[] {2, 3}
                    }));
        }
    }
}