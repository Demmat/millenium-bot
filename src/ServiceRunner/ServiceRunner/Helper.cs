#region

using System;
using System.IO;
using System.Reflection;

#endregion

namespace ServiceRunner
{
    public static class Helper
    {
        public static readonly string LOGFILE = "logservice.txt";
        public static readonly string CONFIGFILE = "config.txt";

        public static void Log(string text)
        {
            try
            {
                StreamWriter sw = File.AppendText(Filename(LOGFILE));
                sw.WriteLine(DateTime.Now.ToString() + " " + text);
                sw.Close();
            }
            catch
            {
            }
        }

        public static string Filename(string filename)
        {
            Assembly a = Assembly.GetEntryAssembly();
            string baseDir = Path.GetDirectoryName(a.Location);
            if (!baseDir.EndsWith(Path.DirectorySeparatorChar.ToString()))
            {
                baseDir += Path.DirectorySeparatorChar;
            }
            return baseDir + filename;
        }

        public static Config ReadConfig()
        {
            try
            {
                var config = new Config
                                 {
                                     ServiceName = "MillenuimBot",
                                     Executable =
                                         Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) +
                                         "\\svote.exe",
                                     ExeArgs = null
                                 };


                return config;
            }
            catch
            {
                return null;
            }
        }

        private static bool IsConfigValid(Config config)
        {
            if (config == null)
            {
                Log("Internal Error: Validation of configuration failed. config was null.");
                return false;
            }

            if (config.ServiceName == null || config.Executable == null)
            {
                Log("Internal Error: Validation of configuration failed. ServiceName or Executable was null.");
                return false;
            }

            if (config.ServiceName.Length > 256 ||
                config.ServiceName.Contains("\\") ||
                config.ServiceName.Contains("/"))
            {
                Log("Error: " + CONFIGFILE +
                    ": Service name (Line 1) must not contain the " +
                    @"characters ""/"" or ""\"" and must not be " +
                    "longer than 256 characters.");
                return false;
            }
            if (!File.Exists(config.Executable))
            {
                Log("Warning: " + CONFIGFILE +
                    ": Executable file (Line 2) does not exist.");
            }
            if (config.ExeArgs != null && config.ExeArgs.Trim().Length == 0)
            {
                Log("Warning: " + CONFIGFILE +
                    ": Program arguments (Line 3): Empty line.");
            }
            return true;
        }

        #region Nested type: Config

        public class Config
        {
            public string ServiceName { get; set; }
            public string Executable { get; set; }
            public string ExeArgs { get; set; }
        }

        #endregion
    }
}