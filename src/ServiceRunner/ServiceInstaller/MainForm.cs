#region

using System;
using System.Diagnostics;
using System.Windows.Forms;
using ServiceRunner;

#endregion

namespace ServiceInstaller
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void buttonInstall_Click(object sender, EventArgs e)
        {
            Helper.Config config = GetConfig();
            if (config == null) return;
            MessageBox.Show(
                Run("sc", "create \"" +
                          config.ServiceName + "\" binpath= \"" +
                          Helper.Filename("MillenuimService.exe") +
                          "\" DisplayName= \"" + config.ServiceName +
                          "\" type= own start= auto"));
        }

        private void buttonUninstall_Click(object sender, EventArgs e)
        {
            Helper.Config config = GetConfig();
            if (config == null) return;
            MessageBox.Show(
                Run("sc", "delete \"" +
                          config.ServiceName + "\""));
        }

        private void buttonStart_Click(object sender, EventArgs e)
        {
            Helper.Config config = GetConfig();
            if (config == null) return;
            MessageBox.Show(
                Run("sc", "start \"" +
                          config.ServiceName + "\""));
        }

        private void buttonStop_Click(object sender, EventArgs e)
        {
            Helper.Config config = GetConfig();
            if (config == null) return;
            MessageBox.Show(
                Run("sc", "stop \"" +
                          config.ServiceName + "\""));
        }

        private string Run(string filename, string arguments)
        {
            try
            {
                var process = new Process();

                Helper.Log("Executing " + filename + " " + arguments);
                process.StartInfo.FileName = filename;
                process.StartInfo.Arguments = arguments;
                process.StartInfo.UseShellExecute = false;
                process.StartInfo.RedirectStandardOutput = true;

                process.Start();

                string output = process.StandardOutput.ReadToEnd();
                Helper.Log("Output: " + output);
                return output;
            }
            catch (Exception ex)
            {
                string msg = "Error: " + ex;
                Helper.Log(msg);
                return msg;
            }
        }

        private Helper.Config GetConfig()
        {
            Helper.Config config = Helper.ReadConfig();
            if (config == null)
            {
                string msg = "Error: invalid or missing configuration file "
                             + Helper.CONFIGFILE + ".";
                Helper.Log(msg);
                MessageBox.Show(msg + " See logfile " + Helper.LOGFILE +
                                " for more information.");
            }
            return config;
        }
    }
}