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

            // 假设日期格式是 "yyyy-MM-dd"，则允许输入的字符只能是数字和短横线
/* if (!char.IsDigit(e.KeyChar) && e.KeyChar != '-' && e.KeyChar != 8 && e.KeyChar != 13)
 {
     // 如果不是数字、短横线、退格键或回车键，则不允许输入
     MessageBox.Show("输入框只能输入日期（格式为yyyy-MM-dd）", "操作提示", MessageBoxButtons.OK,
                     MessageBoxIcon.Information);
     e.Handled = true; // 表示已经处理过KeyPress事件
 }*/



/*
//允许输入数字、小数点及负号（假设只允许在开头输入负号）
if ((e.KeyChar != '-' || (e.KeyChar == '-' && ((TextBox)sender).Text.Length != 0)) &&
    !char.IsDigit(e.KeyChar) && e.KeyChar != '.' && e.KeyChar != 8 && e.KeyChar != 13)
{
    // 如果不是数字、小数点、负号（仅在开头）、退格键或回车键，则不允许输入
    MessageBox.Show("输入框只能输入小数", "操作提示", MessageBoxButtons.OK,
                    MessageBoxIcon.Information);
    e.Handled = true; // 表示已经处理过KeyPress事件
}
else if (e.KeyChar == '.' && ((TextBox)sender).Text.Contains("."))
{
    // 如果已经包含小数点，则不允许再输入小数点
    MessageBox.Show("输入框中已存在小数点", "操作提示", MessageBoxButtons.OK,
                    MessageBoxIcon.Information);
    e.Handled = true; // 表示已经处理过KeyPress事件
}*/

/*

if (e.KeyChar >= 0x4e00 && e.KeyChar <= 0x9fff)
{
    // 如果是汉字则允许输入
    return;
}
else if (char.IsLetterOrDigit(e.KeyChar))
{
    // 如果是字母或数字则弹出提示
    MessageBox.Show("输入框只能输入汉字", "操作提示", MessageBoxButtons.OK,
                    MessageBoxIcon.Information);
    e.Handled = true; // 表示已经处理过KeyPress事件
}
// 这里可以添加其他条件来处理其他非汉字字符，如标点符号等
*/




        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
