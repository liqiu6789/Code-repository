namespace 限定输入类型TextBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar != 8 && !char.IsDigit(e.KeyChar)) && e.KeyChar != 13)
            {
                MessageBox.Show("输入框只能输入数字", "操作提示", MessageBoxButtons.OK,
                MessageBoxIcon.Information);   //弹出信息提示
                e.Handled = true;   //表示已经处理过KeyPress事件
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
