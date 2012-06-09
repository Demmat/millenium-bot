#region

using System;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.ServiceProcess;
using System.Threading;
using System.Timers;
using Timer = System.Timers.Timer;

#endregion

namespace ServiceRunner
{
    public partial class Service : ServiceBase
    {
        private readonly Timer _timer = new Timer();
        private Process _p;

        public Service()
        {
            InitializeComponent();
        }

        protected override void OnStart(string[] args)
        {
            try
            {
                Helper.Log("ServiceRunner service started.");
                StartProcess(null, null);

                _timer.Elapsed += StartProcess;
                _timer.Interval = 1200000; //20min in msec
                _timer.Start();
            }
            catch (Exception ex)
            {
                Helper.Log("Error: " + ex.Message);
            }
        }


        protected void StartProcess(object source, ElapsedEventArgs e)
        {
            try
            {
                _p.Kill();
            }
            catch (Exception ex)
            {
                Helper.Log("Error: " + ex.Message);
            }

            _p = new Process
                     {
                         StartInfo = new ProcessStartInfo
                                         {
                                             FileName =
                                                 Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) +
                                                 "\\svote.exe",
                                             Arguments = null
                                         }
                     };
            _p.Start();


            Helper.Log("Millenuim Bot started.");
            Thread.Sleep(420000);
            try
            {
                _p.Kill();
            }
            catch (Exception ex)
            {
                Helper.Log("Error: " + ex.Message);
            }
        }

        protected override void OnStop()
        {
            try
            {
                if (_p != null)
                {
                    _p.Kill();
                    Helper.Log(_p.StartInfo.FileName + " killed.");
                }
            }
            catch (Exception ex)
            {
                Helper.Log("Error: " + ex.Message);
            }
            Helper.Log("ServiceRunner service stopped.");
        }
    }
}