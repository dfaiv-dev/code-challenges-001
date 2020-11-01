using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

/*
 * Emas super computer: https://www.hackerrank.com/challenges/two-pluses/problem
 */

namespace HackerRank.ProblemSolving
{
    class _001_EmasSuperComputer
    {
        /*
        1 1 0
        1 1 1
        1 1 1
        
        start at 0,0. for each cell, find all valid crosses
        store cross as (origin, size), ie [(0,0), 1], or [(1,1),3]
        find two largest crosses that don't overlap
        
        complexity - all crosses
        n*m for each cell
        - each cell, basically need to check all other cells
        -    (n * m) * (n * m)
        - O(n^4)
        
        find two largest cells that don't overlap
        - brute force - crosses^2, crosses < n
        
        - O(n^4)
        - max 15x15, so probably OK
        
        * find crosses *
        for each cell:
            check cross validity until invalid, odd sizes (1,3,5)
                if valid, add to result (1 will always be valid)
        
        * check cross validity *
            - start_origin
            - size
            - offset = ((size + 1) / 2) - 1
                - (1+1) / 2 - 1 = 0
                - (3+1) / 2 - 1 = 1
                - (5+1) / 2 - 1 = 2
                - (7+1) / 2 - 1 = 3
            - check_if_valid(origin, offset, grid)
        
        * find two largest *
        - sort results by size (sort on insert)
        - from largest to smallest?
        - for cross n, check n-1...1
        -    first find will be largest product of that run
        -       (but maybe not largest of all options):
        -         [9,8,8,7,6,1,1,1,1] (9*1) < (8*8)
        -    keep largest overall result
     */

        public struct Point
        {
            public int X;
            public int Y;

            public Point(int x, int y)
            {
                X = x;
                Y = y;
            }
        }

        public static bool PointsEqual(Point a, Point b)
        {
            return a.X == b.X && a.Y == b.Y;
        }

        public class Cross
        {
            public Point Origin { get; set; }
            public int Size { get; set; }

            public int GetArea()
            {
                return Size * 2 - 1;
            }
        
            public IEnumerable<Point> GetAllCells()
            {
                yield return Origin;
            
                var offset = CrossSizeOffset(Size);
                for (int i = 1; i <= offset; i++)
                {
                    yield return new Point
                    {
                        X = Origin.X, Y = Origin.Y + i
                    };
                    yield return new Point
                    {
                        X = Origin.X, Y = Origin.Y - i
                    };
                    yield return new Point
                    {
                        X = Origin.X + i, Y = Origin.Y
                    };
                    yield return new Point
                    {
                        X = Origin.X - i, Y = Origin.Y
                    };
                }
            }
        }

        public static int CrossSizeOffset(int size) => ((size + 1) / 2) - 1;

        public static bool IsCellGood(Point cell, string[] grid)
        {
            if (cell.X < 0 || cell.Y < 0 ||
                cell.X >= grid[0].Length || cell.Y >= grid.Length)
            {
                return false;
            }

            var cellVal = grid[cell.Y][cell.X];
            return cellVal == 'G';
        }

        public static bool IsValidCross(Point origin, int offset, string[] grid)
        {
            // check x axis, then y axis;
            return IsXAxisValid(origin, offset, grid) && IsYAxisValid(origin, offset, grid);
        }

        public static bool IsXAxisValid(Point origin, int originOffset, string[] grid)
        {
            var xMin = origin.X - originOffset;
            var xMax = origin.X + originOffset;
            if (xMin < 0 || xMax >= grid[0].Length) return false;

            var x = xMin;
            while (x <= xMax)
            {
                if (!IsCellGood(new Point {X = x, Y = origin.Y}, grid)) return false;
                x++;
            }

            return true;
        }

        public static bool IsYAxisValid(Point origin, int originOffset, string[] grid)
        {
            var yMin = origin.Y - originOffset;
            var yMax = origin.Y + originOffset;
            if (yMin < 0 || yMax >= grid.Length) return false;

            var y = yMin;
            while (y <= yMax)
            {
                if (!IsCellGood(new Point {X = origin.X, Y = y}, grid)) return false;
                y++;
            }

            return true;
        }

        public static bool CrossesOverlap(Cross a, Cross b)
        {
            var aCells = a.GetAllCells().ToArray();
            var bCells = b.GetAllCells().ToArray();

            foreach (var aCell in aCells)
            {
                foreach (var bCell in bCells)
                {
                    if (PointsEqual(aCell, bCell)) return true;
                }
            }

            return false;
        }

        public static int GetCrossProduct(Cross a, Cross b)
        {
            return CrossesOverlap(a, b) ? 0 : a.GetArea() * b.GetArea();
        }

        public static List<Cross> FindAllCrosses(string[] grid)
        {
            var results = new List<Cross>();
            for (int y = 0; y < grid.Length; y++)
            {
                var row = grid[y];
                for (int x = 0; x < row.Length; x++)
                {
                    var origin = new Point {X = x, Y = y};
                    var size = 1;
                    while (true)
                    {
                        var offset = CrossSizeOffset(size);
                        var isValid = IsValidCross(origin, offset, grid);
                        if (!isValid) break;
                    
                        results.Add(new Cross
                        {
                            Origin = origin,
                            Size = size
                        });
                        size += 2;
                    }
                }
            }

            return results;
        }
    
        public static int TwoPlusesProxy(string[] grid)
        {
            var results = FindAllCrosses(grid);

            var largestProduct = 0;
            // find largest product
            for (int i = 0; i < results.Count - 1; i++)
            {
                for (int j = i + 1; j < results.Count; j++)
                {
                    var product = GetCrossProduct(results[i], results[j]);
                    if (product > largestProduct) largestProduct = product;
                }
            }

            return largestProduct;
        }

        // Complete the twoPluses function below.
        static int twoPluses(string[] grid)
        {
            return TwoPlusesProxy(grid);
        }

        static void Main(string[] args)
        {
            TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

            string[] nm = Console.ReadLine().Split(' ');

            int n = Convert.ToInt32(nm[0]);

            int m = Convert.ToInt32(nm[1]);

            string[] grid = new string [n];

            for (int i = 0; i < n; i++)
            {
                string gridItem = Console.ReadLine();
                grid[i] = gridItem;
            }

            int result = twoPluses(grid);

            textWriter.WriteLine(result);

            textWriter.Flush();
            textWriter.Close();
        }
    }
}