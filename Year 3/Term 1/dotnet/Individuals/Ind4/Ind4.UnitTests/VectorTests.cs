using System;
using NUnit.Framework;

namespace Ind4.UnitTests
{
    [TestFixture]
    public class VectorTests
    {
        [Test]
        public void Addition_VectorsOfTheSameLength_ReturnsSum()
        {
            Vector[] data = new[]
            {
                new Vector(new double[] { 1, 0 }),
                new Vector(new double[] { -3, 4 }),
                new Vector(new double[] { 1, 2, -3 }),
                new Vector(new double[] { 4, 5, 0 }),
            };
            
            Vector[] actual = new[]
            {
                data[0] + data[1],
                data[2] + data[3],
            };
            
            Vector[] expected = new[]
            {
                new Vector(new double[] { -2, 4 }),
                new Vector(new double[] { 5, 7, -3 }),
            };
            
            Assert.AreEqual(expected[0].Data, actual[0].Data);
            Assert.AreEqual(expected[1].Data, actual[1].Data);
        }
        
        
        [Test]
        public void Addition_VectorsOfDifferentLength_ThrowsException()
        {
            Vector[] data = new[]
            {
                new Vector(new double[] { 1, 0 }),
                new Vector(new double[] { 1, 2, -3 }),
            };

            var ex = Assert.Throws<Exception>(() =>
            {
                var tmp = data[0] + data[1];
            });
            Assert.AreEqual(
                "Lenght of the vectors must be the same to add them", 
                ex.Message);
        }
        
        
        [Test]
        public void ScalarProduct_VectorsOfTheSameLength_ReturnsScalar()
        {
            Vector[] data = new[]
            {
                new Vector(new double[] { 1, 0 }),
                new Vector(new double[] { -3, 4 }),
                new Vector(new double[] { 1, 2, -3 }),
                new Vector(new double[] { 4, 5, 0 }),
            };
            
            double[] actual = new[]
            {
                data[0] * data[1],
                data[2] * data[3],
            };
            
            double[] expected = new[]
            {
                -3.0,
                14.0,
            };
            
            Assert.AreEqual(expected, actual);
        }
        
        
        [Test]
        public void ScalarProduct_VectorsOfDifferentLength_ThrowsException()
        {
            Vector[] data = new[]
            {
                new Vector(new double[] { 1, 0 }),
                new Vector(new double[] { 1, 2, -3 }),
            };

            var ex = Assert.Throws<Exception>(() =>
            {
                var tmp = data[0] * data[1];
            });
            Assert.AreEqual(
                "Lenght of the vectors must be the same to calculate Scalar product", 
                ex.Message);
        }
        
        
        [Test]
        public void Multiply_VectorByConst_ReturnsScaledVectorByConst()
        {
            Vector[] vectorsData = new[]
            {
                new Vector(new double[] { 1, 0 }),
                new Vector(new double[] { -3, 4 }),
                new Vector(new double[] { 1, 2, -3 }),
                new Vector(new double[] { 4, 5, 0 }),
            };

            double[] constData = new[]
            {
                2.0,
                3.0,
                -4.5,
                0
            };
                
            Vector[] actual = new[]
            {
                vectorsData[0] * constData[0],
                constData[1] * vectorsData[1],
                vectorsData[2] * constData[2],
                constData[3] * vectorsData[3],
            };
            
            Vector[] expected = new[]
            {
                new Vector(new double[] { 2, 0 }),
                new Vector(new double[] { -9, 12 }),
                new Vector(new double[] { -4.5, -9, 13.5 }),
                new Vector(new double[] { 0, 0, 0 }),
            };
            
            Assert.AreEqual(expected[0].Data, actual[0].Data);
            Assert.AreEqual(expected[1].Data, actual[1].Data);
            Assert.AreEqual(expected[2].Data, actual[2].Data);
            Assert.AreEqual(expected[3].Data, actual[3].Data);
        }
        
        
        [Test]
        public void ToString_ReturnsStringRepresentation()
        {
            Vector[] data = new[]
            {
                new Vector(),
                new Vector(2),
                new Vector(new double[] { 2, -3}),
                new Vector(new double[] { 4, 5, 0 }),
            };
            
            string[] actual = new[]
            {
                data[0].ToString(),
                data[1].ToString(),
                data[2].ToString(),
                data[3].ToString(),
            };
            
            string[] expected = new[]
            {
                "[]",
                "[0 0]",
                "[2 -3]",
                "[4 5 0]"
            };
            
            Assert.AreEqual(expected, actual);
        }


        [Test] public void Getter_IndexInsideTheBounds_ReturnsElementAtIndex()
        {
            Vector[] data = new[]
            {
                new Vector(new double[] { 1, 0 }),
                new Vector(new double[] { -3, 4 }),
                new Vector(new double[] { 1, 2, -3 }),
                new Vector(new double[] { 4, 5, 0 }),
            };
            
            double[] actual = new[]
            {
                data[0][0],
                data[1][0],
                data[2][2],
                data[3][-2],
            };
            
            double[] expected = new[]
            {
                1.0,
                -3.0,
                -3.0,
                5.0,
            };
            
            Assert.AreEqual(expected, actual);
        }
        
        
        [Test] public void Getter_IndexOutsideTheBounds_ThrowsException()
        {
            var v1 = new Vector(new double[] { 1, 0 });
            
            var ex = Assert.Throws<Exception>(() =>
            {
                v1[3] = 2;
            });
            Assert.AreEqual(
                "Index is outside the bounds of vector", 
                ex.Message);
        }
        
        
        [Test] public void Setter_IndexInsideTheBounds_SetsElementAtIndex()
        {
            var v1 = new Vector(4);

            v1[0] = 1;
            v1[1] = 2;
            v1[-1] = -3;
            v1[-2] = 0;
            
            
            double[] actual = new[]
            {
                v1[0],
                v1[1],
                v1[-1],
                v1[-2]
            };
            
            double[] expected = new[]
            {
                1.0,
                2.0,
                -3.0,
                0.0
            };
            
            Assert.AreEqual(expected, actual);
        }
        
        
        [Test] public void Setter_IndexOutsideTheBounds_ThrowsException()
        {
            var v1 = new Vector(new double[] { 1, 0 });

            var ex = Assert.Throws<Exception>(() =>
            {
                v1[3] = 2;
            });
            Assert.AreEqual(
                "Index is outside the bounds of vector", 
                ex.Message);
        }
    }
}
