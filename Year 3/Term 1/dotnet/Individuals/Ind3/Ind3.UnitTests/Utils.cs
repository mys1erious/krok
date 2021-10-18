using System;

namespace Ind3.UnitTests

{
    public static class Utils
    {
        public static double GetTolerance(double val)
        {
            int magnitude = 1 + (val == 0.0 ? -1 : Convert.ToInt32(Math.Floor(Math.Log10(val))));
            int precision = 15 - magnitude;
            double tolerance = 1.0 / Math.Pow(10, precision);

            return tolerance;
        }
    }
}