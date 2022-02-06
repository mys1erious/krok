using System;

namespace VectorDemo
{
    public class Vector
    {
        private double[] data;

        public Vector()
        {
            
        }
        
        public Vector(int N)
        {
            throw new NotImplementedException();
        }
        
        public Vector(double[] d)
        {
            throw new NotImplementedException();
        }

        public Vector Add(Vector o)
        {
            throw new NotImplementedException();
        }
        
        public Vector Sub(Vector o)
        {
            throw new NotImplementedException();
        }
        
        public double Scalar(Vector o)
        {
            throw new NotImplementedException();
        }
        
        public static Vector operator*(Vector v, double c)
        {
            throw new NotImplementedException();
        }
        
        public static Vector operator*(double c,Vector v)
        {
            return v * c;
        }

        public override string ToString()
        {
            throw new NotImplementedException();
        }

        public int Count { get; set; }

        public double this[int index]
        {
            get
            {
                return data[index];
            }

            set
            {
                data[index] = value;
            }
        }
    }
}