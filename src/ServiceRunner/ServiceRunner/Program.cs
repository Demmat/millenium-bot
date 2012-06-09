#region

using System.ServiceProcess;

#endregion

namespace ServiceRunner
{
    internal static class Program
    {
        /// <summary>
        ///   Der Haupteinstiegspunkt für die Anwendung.
        /// </summary>
        private static void Main()
        {
            var servicesToRun = new ServiceBase[]
                                    {
                                        new Service()
                                    };
            ServiceBase.Run(servicesToRun);
        }
    }
}