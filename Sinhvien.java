public class Sinhvien {
    String maSv;
    String hoTen;
    int tuoi;
    static int soLuong = 0;
    public Sinhvien(){
        soLuong ++;
    }
    public void setThongtin(String maSv, String hoTen, int tuoi){
        this.maSv = maSv;
        this.hoTen = hoTen;
        this.tuoi = tuoi;
    }
    public void hienthithontin(){
        System.out.printf("Tên: %s | mã sinh viên: %s | tuổi: %d",this.hoTen,this.maSv,this.soLuong);
    }
    public static void hienthisoluong(){
        System.out.println(soLuong);
    }


}
