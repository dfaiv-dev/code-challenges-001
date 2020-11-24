using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

namespace HackerRank.ProblemSolving
{
    // https://www.hackerrank.com/challenges/count-luck/problem
    
    /*
        Example Maze (start at M, end at *):
        .X.X......X
        .X*.X.XXX.X
        .XX.X.XM...
        ......XXXX.
        
        Find # of decision points
        
        - find M
        - foreach point
     */
    
    public class _002_CountLuck_DFS
    {
        public static string CountLuckProxy(string[] matrix, int k)
        {
            return "not implemented";
        }

        // Complete the countLuck function below.
        static string countLuck(string[] matrix, int k)
        {
            return CountLuckProxy(matrix, k);
        }

        static void Main(string[] args) {
            TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

            int t = Convert.ToInt32(Console.ReadLine());

            for (int tItr = 0; tItr < t; tItr++) {
                string[] nm = Console.ReadLine().Split(' ');

                int n = Convert.ToInt32(nm[0]);

                int m = Convert.ToInt32(nm[1]);

                string[] matrix = new string [n];

                for (int i = 0; i < n; i++) {
                    string matrixItem = Console.ReadLine();
                    matrix[i] = matrixItem;
                }

                int k = Convert.ToInt32(Console.ReadLine());

                string result = countLuck(matrix, k);

                textWriter.WriteLine(result);
            }

            textWriter.Flush();
            textWriter.Close();
        }
    }

}