using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using Xunit;

namespace HackerRank.InterviewPrep
{
    /// <summary>
    /// https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
    /// </summary>
    public class ArrayManipulation
    {
        // Complete the arrayManipulation function below.
        static long arrayManipulation(int n, int[][] queries)
        {
            // FAIL: Wrong answers
            // FAIL: Time limits

            // add initial, single range, with val 0
            var sortedRanges = new List<int> {1};
            var rangeValues = new List<long> {0};

            foreach (var query in queries)
            {
                var rangeMin = query[0];
                var rangeMax = query[1];
                var val = query[2];

                var rangeMinIndex = sortedRanges.BinarySearch(rangeMin);
                if (rangeMinIndex < 0)
                {
                    rangeMinIndex = ~rangeMinIndex;
                    sortedRanges.Insert(rangeMinIndex, rangeMin);
                    rangeValues.Insert(rangeMinIndex, rangeValues[rangeMinIndex - 1]);
                }

                var rangeMaxIndex = sortedRanges.BinarySearch(rangeMax);
                if (rangeMaxIndex < 0)
                {
                    rangeMaxIndex = ~rangeMaxIndex;
                    sortedRanges.Insert(rangeMaxIndex, rangeMax);
                    rangeValues.Insert(rangeMaxIndex, rangeValues[rangeMaxIndex - 1]);
                    sortedRanges.Insert(rangeMaxIndex + 1, rangeMax + 1);
                    rangeValues.Insert(rangeMaxIndex + 1, 0);
                }

                for (int i = rangeMinIndex; i <= rangeMaxIndex; i++)
                {
                    rangeValues[i] = rangeValues[i] + val;
                }
            }

            var result = rangeValues.Max();
            return result;
        }

        public class TestCases
        {
            [Fact]
            public void TestCase0()
            {
                var result = ArrayManipulation.arrayManipulation(5, new[]
                {
                    new[] {1, 2, 100},
                    new[] {2, 5, 100},
                    new[] {3, 4, 100}
                });

                Assert.Equal(200, result);
            }
        }
    }
}