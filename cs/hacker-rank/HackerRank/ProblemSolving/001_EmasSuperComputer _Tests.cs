using System;
using System.Linq;
using Xunit;

/*
 * Emas super computer: https://www.hackerrank.com/challenges/two-pluses/problem
 */

namespace HackerRank.ProblemSolving
{
    public class SolutionTests
    {
        [Fact]
        public void TestCase03()
        {
            var result = _001_EmasSuperComputer.TwoPlusesProxy(
                new[]
                {
                    "GBGBGGB",
                    "GBGBGGB",
                    "GBGBGGB",
                    "GGGGGGG",
                    "GGGGGGG",
                    "GBGBGGB",
                    "GBGBGGB"
                });
            Assert.Equal(45, result);
        }

        [Fact]
        public void TestCase12()
        {
            // ReSharper disable StringLiteralTypo
            var grid = ParseGrid(@"
GGBBGBBGBBG
GGBBGBBGBBG
GGGGGGGGGGG
GGBBGBBGBBG
GGGGGGGGGGG
GGBBGBBGBBG
GGBBGBBGBBG
GGGGGGGGGGG
GGBBGBBGBBG
GGGGGGGGGGG
GGBBGBBGBBG
GGBBGBBGBBG
GGBBGBBGBBG
");
            // ReSharper restore StringLiteralTypo

            var result = _001_EmasSuperComputer.TwoPlusesProxy(grid);
            Assert.Equal(221, result);
        }
        
        [Fact]
        public void TestCase12_FindAllCrosses()
        {
            // ReSharper disable StringLiteralTypo
            var grid = ParseGrid(@"
GGBBGBBGBBG
GGBBGBBGBBG
GGGGGGGGGGG
GGBBGBBGBBG
GGGGGGGGGGG
GGBBGBBGBBG
GGBBGBBGBBG
GGGGGGGGGGG
GGBBGBBGBBG
GGGGGGGGGGG
GGBBGBBGBBG
GGBBGBBGBBG
GGBBGBBGBBG
");
            // ReSharper restore StringLiteralTypo

            var result = _001_EmasSuperComputer.FindAllCrosses(grid);
            var resultCount = result.Count;
            Assert.Equal(117, resultCount);
        }


        private static string[] ParseGrid(string gridRaw)
        {
            return gridRaw.Trim()
                .Split(new[] {"\n"}, StringSplitOptions.RemoveEmptyEntries)
                .ToArray();
        }

        [Fact]
        public void WHEN_CrossesOverlap()
        {
            var result = _001_EmasSuperComputer.CrossesOverlap(
                new _001_EmasSuperComputer.Cross
                {
                    Origin = new _001_EmasSuperComputer.Point(2, 3),
                    Size = 5
                },
                new _001_EmasSuperComputer.Cross
                {
                    Origin = new _001_EmasSuperComputer.Point(2, 4),
                    Size = 5
                });

            Assert.True(result);
        }
    }
}