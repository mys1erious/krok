using System;
using System.Collections.Generic;
using NUnit.Framework;

namespace Ind3.UnitTests

{
    [TestFixture]
    public class Ind3Tests
    {
        [Test]
        public void Task_1_17_m_Test()
        {
            double[] expected =
            {
                4.56549,
                5.38362,
                5.10543,
                10.39860
            };
            double tolerance = 0.00001;
            
            
            double[] actual =
            {
                Ind3.Task_1_17_m(2, 3, 4), 
                Ind3.Task_1_17_m(8, 10, 12),
                Ind3.Task_1_17_m(6, 4, 1),
                Ind3.Task_1_17_m(12, 4, -1)
            };

            
            Assert.That(actual[0], Is.EqualTo(expected[0]).Within(tolerance));
            Assert.That(actual[1], Is.EqualTo(expected[1]).Within(tolerance));
            Assert.That(actual[2], Is.EqualTo(expected[2]).Within(tolerance));
            Assert.That(actual[3], Is.EqualTo(expected[3]).Within(tolerance));
        }
        
        
        [Test]
        public void Task_3_2_v_Test()
        {
            bool[] actual =
            {
                Ind3.Task_3_2_v(false, true, false), 
                Ind3.Task_3_2_v(false, false, false),
                Ind3.Task_3_2_v(true, true, true),
                Ind3.Task_3_2_v(false, true, true)
            };

            
            Assert.IsFalse(actual[0]);
            Assert.IsFalse(actual[1]);
            Assert.IsTrue(actual[2]);
            Assert.IsFalse(actual[3]);
        }
        
        
        [Test]
        public void Task_3_6_e_Test()
        {
            bool[] actual =
            {
                Ind3.Task_3_6_e(false, false, true), 
                Ind3.Task_3_6_e(false, false, false),
                Ind3.Task_3_6_e(true, true, true),
                Ind3.Task_3_6_e(false, true, true)
            };


            Assert.IsFalse(actual[0]);
            Assert.IsTrue(actual[1]);
            Assert.IsTrue(actual[2]);
            Assert.IsFalse(actual[3]);
        }
        
        
        [Test]
        public void Task_3_12_d_Test()
        {
            bool[] actual =
            {
                Ind3.Task_3_12_d(2, 1),
                Ind3.Task_3_12_d(1, 2),
                Ind3.Task_3_12_d(1, 0),
                Ind3.Task_3_12_d(-1, 0)
            };


            Assert.IsTrue(actual[0]);
            Assert.IsTrue(actual[1]);
            Assert.IsTrue(actual[2]);
            Assert.IsFalse(actual[3]);
        }
        
        
        [Test]
        public void Task_3_29_e_Test()
        {
            bool[] actual =
            {
                Ind3.Task_3_29_e(101, 1, 0),
                Ind3.Task_3_29_e(1, 101, 1),
                Ind3.Task_3_29_e(1, 1, 101),
                Ind3.Task_3_29_e(-1, 1, 1)
            };


            Assert.IsTrue(actual[0]);
            Assert.IsTrue(actual[1]);
            Assert.IsTrue(actual[2]);
            Assert.IsFalse(actual[3]);
        }
        
        
        [Test]
        public void Task_4_8_Test()
        {
            int[] actual =
            {
                Ind3.Task_4_8(1, 3000),
                Ind3.Task_4_8(3000, 1),
                Ind3.Task_4_8(0.45, 1000),
                Ind3.Task_4_8(-1, -1)
            };


            Assert.AreEqual(1, actual[0]);
            Assert.AreEqual(2, actual[1]);
            Assert.AreEqual(1, actual[2]);
            Assert.AreEqual(-1, actual[3]);
        }
        
        
        [Test]
        public void Task_4_97_Test()
        {
            string[] actual =
            {
                Ind3.Task_4_97(1),
                Ind3.Task_4_97(4),
                Ind3.Task_4_97(8),
                Ind3.Task_4_97(22)
            };


            Assert.AreEqual("Winter", actual[0]);
            Assert.AreEqual("Spring", actual[1]);
            Assert.AreEqual("Summer", actual[2]);
            Assert.AreEqual("", actual[3]);
        }
        
        
        [Test]
        public void Task_5_17_Test()
        {
            double[][] expected =
            {
                new double[]{32.5, 52},
                new double[]{75.5, 103},
                new double[]{5.5, -2},
                new double[]{-5.5, -5}
            };


            double[][] actual =
            {
                Ind3.Task_5_17(new double[]{1, 2}), 
                Ind3.Task_5_17(new double[]{3, 4}),
                Ind3.Task_5_17(new double[]{-1, -2}),
                Ind3.Task_5_17(new double[]{-3, -4})
            };
            

            Assert.AreEqual(expected[0], actual[0]);
            Assert.AreEqual(expected[1], actual[1]);
            Assert.AreEqual(expected[2], actual[2]);
            Assert.AreEqual(expected[3], actual[3]);
        }
        
        
        [Test]
        public void Task_6_28_a_Test()
        {
            Assert.AreEqual(new int[]{0, 0},Ind3.Task_6_28_a(1));
            Assert.AreEqual(new int[]{3, 5},Ind3.Task_6_28_a(123945678));
            
            var ex1 = Assert.Throws<ArgumentException>(() => Ind3.Task_6_28_a(0));
            Assert.AreEqual("Input value has to be > 0", ex1.Message);

            var ex2 = Assert.Throws<ArgumentException>(() => Ind3.Task_6_28_a(122));
            Assert.AreEqual("Input value contains duplicates, its not allowed", ex2.Message);
        }


        [Test]
        public void Task_7_10_Test()
        {
            int[][] expected =
            {
                new int[] {16, 18, 24, 28, 32, 38, 40, 48, 56, 58, 64, 68, 72, 78, 
                           80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 96, 98},
                new int[] {16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96},
                new int[] {12, 24, 36, 48, 60, 72, 84, 96}
            };
            

            List<int>[] actual =
            {
                Ind3.Task_7_10(8), 
                Ind3.Task_7_10(-8),
                Ind3.Task_7_10(12),
            };
            
            
            Assert.AreEqual(expected[0], actual[0]);
            Assert.AreEqual(expected[1], actual[1]);
            Assert.AreEqual(expected[2], actual[2]);

            var ex = Assert.Throws<ArgumentException>(() => Ind3.Task_7_10(0));
            Assert.AreEqual("Input value cant be 0", ex.Message);
        }
        
        
        //Task_8_4_v Test ? !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        
        [Test]
        public void Task_11_19_a_Test()
        {
            int[] expected = new[] { 6, 15, -15, 312};
            
            
            int[] actual =
            {
                Ind3.Task_11_19_a(new int[] { 1, 2, 3 }),
                Ind3.Task_11_19_a(new int[] { 4, 5, 6 }),
                Ind3.Task_11_19_a(new int[] { -4, -5, -6 }),
                Ind3.Task_11_19_a(new int[] { 301, 11, 0 })
            };
            
            
            Assert.AreEqual(expected[0],actual[0]);
            Assert.AreEqual(expected[1],actual[1]);
            Assert.AreEqual(expected[2],actual[2]);
            Assert.AreEqual(expected[3],actual[3]);
        }


        [Test]
        public void Task_11_44_Test()
        {
            int[][] expected =
            {
                new int[]{0, 4, 5, 7, 11, 12, 16, 18},
                new int[]{7, 10, 14, 16, 19},
                new int[]{0, 1, 6, 14, 15},
                new int[]{7, 8, 19}
            };


            int[][] data =
            {
                new int[]{1, 9, 4, 9, 0, 1, 4, 1, 5, 7, 6, 2, 2, 5, 8, 9, 0, 4, 1, 4},
                new int[]{8, 3, 3, 3, 3, 3, 9, 2, 5, 6, 0, 9, 7, 5, 1, 5, 2, 7, 4, 1},
                new int[]{1, 1, 5, 8, 8, 3, 2, 6, 6, 9, 6, 3, 6, 6, 1, 0, 5, 4, 4, 3},
                new int[]{4, 7, 8, 5, 6, 9, 6, 1, 1, 3, 8, 8, 7, 4, 4, 7, 6, 9, 3, 1},
            };
            int[][] actual =
            {
                Ind3.Task_11_44(data[0]),
                Ind3.Task_11_44(data[1]),
                Ind3.Task_11_44(data[2]),
                Ind3.Task_11_44(data[3]),
            };
            
            
            Assert.AreEqual(expected[0],actual[0]);
            Assert.AreEqual(expected[1],actual[1]);
            Assert.AreEqual(expected[2],actual[2]);
            Assert.AreEqual(expected[3],actual[3]);
        }


        [Test]
        public void Task_12_25_z_Test()
        {
            int[,] expected = new int[,]
            {
                { 109, 97, 85, 73, 61, 49, 37, 25, 13, 1 },
                { 110, 98, 86, 74, 62, 50, 38, 26, 14, 2 },
                { 111, 99, 87, 75, 63, 51, 39, 27, 15, 3 },
                { 112, 100, 88, 76, 64, 52, 40, 28, 16, 4 },
                { 113, 101, 89, 77, 65, 53, 41, 29, 17, 5 },
                { 114, 102, 90, 78, 66, 54, 42, 30, 18, 6 },
                { 115, 103, 91, 79, 67, 55, 43, 31, 19, 7 },
                { 116, 104, 92, 80, 68, 56, 44, 32, 20, 8 },
                { 117, 105, 93, 81, 69, 57, 45, 33, 21, 9 },
                { 118, 106, 94, 82, 70, 58, 46, 34, 22, 10 },
                { 119, 107, 95, 83, 71, 59, 47, 35, 23, 11 },
                { 120, 108, 96, 84, 72, 60, 48, 36, 24, 12 },
            };
            
            
            Assert.AreEqual(expected, Ind3.Task_12_25_z());
        }
    }
}