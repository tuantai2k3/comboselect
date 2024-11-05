from django.shortcuts import render, get_object_or_404, redirect
from .models import Phim
from .forms import PhimForm
from django.shortcuts import render
from .forms import ComboSelectionForm

def home(request):
    return render(request, 'home.html')  # Render a home page template


# View để hiển thị danh sách phim
def danh_sach_phim(request):
    ds_phim = Phim.objects.all()
    return render(request, 'base/danh_sach_phim.html', {'ds_phim': ds_phim})

# View để thêm phim
def them_phim(request):
    if request.method == 'POST':
        form = PhimForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_phim')
    else:
        form = PhimForm()
    return render(request, 'base/them_phim.html', {'form': form})

# View để sửa phim
def sua_phim(request, id):
    phim = get_object_or_404(Phim, id=id)
    if request.method == 'POST':
        form = PhimForm(request.POST, instance=phim)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_phim')
    else:
        form = PhimForm(instance=phim)
    return render(request, 'base/sua_phim.html', {'form': form})

# View để xóa phim
def xoa_phim(request, id):
    phim = get_object_or_404(Phim, id=id)
    if request.method == 'POST':
        phim.delete()
        return redirect('danh_sach_phim')
    return render(request, 'base/xoa_phim.html', {'phim': phim})
#comboselect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Combo
from .forms import ComboForm
# View để thêm combo
def them_combo(request):
    if request.method == 'POST':
        form = ComboForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_combo')  # Đường dẫn đến danh sách combo
    else:
        form = ComboForm()
    return render(request, 'base/them_combo.html', {'form': form})

# View để sửa combo
def sua_combo(request, id):
    combo = get_object_or_404(Combo, id=id)
    if request.method == 'POST':
        form = ComboForm(request.POST, instance=combo)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_combo')  # Đường dẫn đến danh sách combo
    else:
        form = ComboForm(instance=combo)
    return render(request, 'base/sua_combo.html', {'form': form})

# View để hiển thị danh sách combo
def danh_sach_combo(request):
    combos = Combo.objects.all()
    return render(request, 'base/danh_sach_combo.html', {'combos': combos})

def select_combo(request):
    if request.method == 'POST':
        form = ComboSelectionForm(request.POST)
        if form.is_valid():
            selected_combo = form.cleaned_data['combo']
            # Lưu lựa chọn combo vào session hoặc xử lý theo nhu cầu
            request.session['selected_combo'] = selected_combo.id
            return redirect('next_step')  # Điều hướng tới bước tiếp theo trong quy trình đặt vé
    else:
        form = ComboSelectionForm()
    return render(request, 'comboselect/select_combo.html', {'form': form})

from .models import NguoiDung
from .forms import NguoiDungForm

# View để hiển thị danh sách người dùng
def danh_sach_nguoi_dung(request):
    ds_nguoi_dung = NguoiDung.objects.all()
    return render(request, 'base/danh_sach_nguoi_dung.html', {'ds_nguoi_dung': ds_nguoi_dung})

# View để thêm người dùng
def them_nguoi_dung(request):
    if request.method == 'POST':
        form = NguoiDungForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_nguoi_dung')
    else:
        form = NguoiDungForm()
    return render(request, 'base/them_nguoi_dung.html', {'form': form})

# View để sửa người dùng
def sua_nguoi_dung(request, id):
    nguoi_dung = get_object_or_404(NguoiDung, id=id)
    if request.method == 'POST':
        form = NguoiDungForm(request.POST, instance=nguoi_dung)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_nguoi_dung')
    else:
        form = NguoiDungForm(instance=nguoi_dung)
    return render(request, 'base/sua_nguoi_dung.html', {'form': form})

# View để xóa người dùng
def xoa_nguoi_dung(request, id):
    nguoi_dung = get_object_or_404(NguoiDung, id=id)
    if request.method == 'POST':
        nguoi_dung.delete()
        return redirect('danh_sach_nguoi_dung')
    return render(request, 'base/xoa_nguoi_dung.html', {'nguoi_dung': nguoi_dung})



from .models import TheLoai
from .forms import TheLoaiForm

# View để hiển thị danh sách thể loại
def danh_sach_the_loai(request):
    ds_the_loai = TheLoai.objects.all()
    return render(request, 'base/danh_sach_the_loai.html', {'ds_the_loai': ds_the_loai})

# View để thêm thể loại
def them_the_loai(request):
    if request.method == 'POST':
        form = TheLoaiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_the_loai')
    else:
        form = TheLoaiForm()
    return render(request, 'base/them_the_loai.html', {'form': form})

# View để sửa thể loại
def sua_the_loai(request, id):
    the_loai = get_object_or_404(TheLoai, id=id)
    if request.method == 'POST':
        form = TheLoaiForm(request.POST, instance=the_loai)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_the_loai')
    else:
        form = TheLoaiForm(instance=the_loai)
    return render(request, 'base/sua_the_loai.html', {'form': form})

# View để xóa thể loại
def xoa_the_loai(request, id):
    the_loai = get_object_or_404(TheLoai, id=id)
    if request.method == 'POST':
        the_loai.delete()
        return redirect('danh_sach_the_loai')
    return render(request, 'base/xoa_the_loai.html', {'the_loai': the_loai})


from .models import DinhDangPhim
from .forms import DinhDangPhimForm

# View hiển thị danh sách định dạng phim
def danh_sach_dinh_dang_phim(request):
    ds_dinh_dang_phim = DinhDangPhim.objects.all()
    return render(request, 'base/danh_sach_dinh_dang_phim.html', {'ds_dinh_dang_phim': ds_dinh_dang_phim})

# View thêm định dạng phim
def them_dinh_dang_phim(request):
    if request.method == 'POST':
        form = DinhDangPhimForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_dinh_dang_phim')
    else:
        form = DinhDangPhimForm()
    return render(request, 'base/them_dinh_dang_phim.html', {'form': form})

# View sửa định dạng phim
def sua_dinh_dang_phim(request, id):
    dinh_dang_phim = get_object_or_404(DinhDangPhim, id=id)
    if request.method == 'POST':
        form = DinhDangPhimForm(request.POST, instance=dinh_dang_phim)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_dinh_dang_phim')
    else:
        form = DinhDangPhimForm(instance=dinh_dang_phim)
    return render(request, 'base/sua_dinh_dang_phim.html', {'form': form})

# View xóa định dạng phim
def xoa_dinh_dang_phim(request, id):
    dinh_dang_phim = get_object_or_404(DinhDangPhim, id=id)
    if request.method == 'POST':
        dinh_dang_phim.delete()
        return redirect('danh_sach_dinh_dang_phim')
    return render(request, 'base/xoa_dinh_dang_phim.html', {'dinh_dang_phim': dinh_dang_phim})



from django.shortcuts import render, get_object_or_404, redirect
from .models import RapChieu
from .forms import RapChieuForm

# View hiển thị danh sách rạp chiếu
def danh_sach_rap_chieu(request):
    ds_rap_chieu = RapChieu.objects.all()
    return render(request, 'base/danh_sach_rap_chieu.html', {'ds_rap_chieu': ds_rap_chieu})

# View thêm rạp chiếu
def them_rap_chieu(request):
    if request.method == 'POST':
        form = RapChieuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_rap_chieu')
    else:
        form = RapChieuForm()
    return render(request, 'base/them_rap_chieu.html', {'form': form})

# View sửa rạp chiếu
def sua_rap_chieu(request, id):
    rap_chieu = get_object_or_404(RapChieu, id=id)
    if request.method == 'POST':
        form = RapChieuForm(request.POST, instance=rap_chieu)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_rap_chieu')
    else:
        form = RapChieuForm(instance=rap_chieu)
    return render(request, 'base/sua_rap_chieu.html', {'form': form})

# View xóa rạp chiếu
def xoa_rap_chieu(request, id):
    rap_chieu = get_object_or_404(RapChieu, id=id)
    if request.method == 'POST':
        rap_chieu.delete()
        return redirect('danh_sach_rap_chieu')
    return render(request, 'base/xoa_rap_chieu.html', {'rap_chieu': rap_chieu})


from .models import XuatChieu
from .forms import XuatChieuForm

# View hiển thị danh sách xuất chiếu
def danh_sach_xuat_chieu(request):
    ds_xuat_chieu = XuatChieu.objects.all()
    return render(request, 'base/danh_sach_xuat_chieu.html', {'ds_xuat_chieu': ds_xuat_chieu})

# View thêm xuất chiếu
def them_xuat_chieu(request):
    if request.method == 'POST':
        form = XuatChieuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_xuat_chieu')
    else:
        form = XuatChieuForm()
    return render(request, 'base/them_xuat_chieu.html', {'form': form})

# View sửa xuất chiếu
def sua_xuat_chieu(request, id):
    xuat_chieu = get_object_or_404(XuatChieu, id=id)
    if request.method == 'POST':
        form = XuatChieuForm(request.POST, instance=xuat_chieu)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_xuat_chieu')
    else:
        form = XuatChieuForm(instance=xuat_chieu)
    return render(request, 'base/sua_xuat_chieu.html', {'form': form})

# View xóa xuất chiếu
def xoa_xuat_chieu(request, id):
    xuat_chieu = get_object_or_404(XuatChieu, id=id)
    if request.method == 'POST':
        xuat_chieu.delete()
        return redirect('danh_sach_xuat_chieu')
    return render(request, 'base/xoa_xuat_chieu.html', {'xuat_chieu': xuat_chieu})



# from .models import Ve, Phim, XuatChieu, NguoiDung
# from .forms import VeForm

# # View hiển thị danh sách vé
# def danh_sach_ve(request):
#     ds_ve = Ve.objects.all()
#     return render(request, 'base/danh_sach_ve.html', {'ds_ve': ds_ve})

# # View thêm vé
# def them_ve(request):
#     if request.method == 'POST':
#         form = VeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('danh_sach_ve')
#     else:
#         form = VeForm()
#     return render(request, 'base/them_ve.html', {'form': form})

# # View sửa vé
# def sua_ve(request, id):
#     ve = get_object_or_404(Ve, id=id)
#     if request.method == 'POST':
#         form = VeForm(request.POST, instance=ve)
#         if form.is_valid():
#             form.save()
#             return redirect('danh_sach_ve')
#     else:
#         form = VeForm(instance=ve)
#     return render(request, 'base/sua_ve.html', {'form': form})

# # View xóa vé
# def xoa_ve(request, id):
#     ve = get_object_or_404(Ve, id=id)
#     if request.method == 'POST':
#         ve.delete()
#         return redirect('danh_sach_ve')
#     return render(request, 'base/xoa_ve.html', {'ve': ve})

#View Quản lý web bán vé
def quan_ly(request):
    return render(request, 'base/introduce.html')


from .models import Ve
from .forms import VeForm

# View hiển thị danh sách vé
def danh_sach_ve(request):
    ds_ve = Ve.objects.all()
    return render(request, 'base/danh_sach_ve.html', {'ds_ve': ds_ve})

# View thêm vé
def them_ve(request):
    if request.method == 'POST':
        form = VeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_ve')
    else:
        form = VeForm()
    return render(request, 'base/them_ve.html', {'form': form})

# View sửa vé
def sua_ve(request, id):
    ve = get_object_or_404(Ve, id=id)
    if request.method == 'POST':
        form = VeForm(request.POST, instance=ve)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_ve')
    else:
        form = VeForm(instance=ve)
    return render(request, 'base/sua_ve.html', {'form': form})

# View xóa vé
def xoa_ve(request, id):
    ve = get_object_or_404(Ve, id=id)
    if request.method == 'POST':
        ve.delete()
        return redirect('danh_sach_ve')
    return render(request, 'base/xoa_ve.html', {'ve': ve})



from .models import GheNgoi
from .forms import GheNgoiForm

# View hiển thị danh sách ghế ngồi
def danh_sach_ghe_ngoi(request):
    ds_ghe = GheNgoi.objects.all()
    return render(request, 'base/danh_sach_ghe_ngoi.html', {'ds_ghe': ds_ghe})

# View thêm ghế ngồi
def them_ghe_ngoi(request):
    if request.method == 'POST':
        form = GheNgoiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_ghe_ngoi')
    else:
        form = GheNgoiForm()
    return render(request, 'base/them_ghe_ngoi.html', {'form': form})

# View sửa ghế ngồi
def sua_ghe_ngoi(request, id):
    ghe = get_object_or_404(GheNgoi, id=id)
    if request.method == 'POST':
        form = GheNgoiForm(request.POST, instance=ghe)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_ghe_ngoi')
    else:
        form = GheNgoiForm(instance=ghe)
    return render(request, 'base/sua_ghe_ngoi.html', {'form': form})

# View xóa ghế ngồi
def xoa_ghe_ngoi(request, id):
    ghe = get_object_or_404(GheNgoi, id=id)
    if request.method == 'POST':
        ghe.delete()
        return redirect('danh_sach_ghe_ngoi')
    return render(request, 'base/xoa_ghe_ngoi.html', {'ghe': ghe})

# Danh sách Combo
def danh_sach_combo(request):
    combos = Combo.objects.all()
    return render(request, 'base/danh_sach_combo.html', {'combos': combos})

# Thêm Combo
def them_combo(request):
    if request.method == 'POST':
        form = ComboForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_combo')
    else:
        form = ComboForm()
    return render(request, 'base/them_combo.html', {'form': form})

# Sửa Combo
def sua_combo(request, id):
    combo = get_object_or_404(Combo, id=id)
    if request.method == 'POST':
        form = ComboForm(request.POST, instance=combo)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_combo')
    else:
        form = ComboForm(instance=combo)
    return render(request, 'base/sua_combo.html', {'form': form})

# Xóa Combo
def xoa_combo(request, id):
    combo = get_object_or_404(Combo, id=id)
    if request.method == 'POST':
        combo.delete()
        return redirect('danh_sach_combo')
    return render(request, 'base/xoa_combo.html', {'combo': combo})


#SELECTCOMBODB
from django.shortcuts import render
from .models import Combo
def select_combo(request):
    # Lấy tất cả dữ liệu từ bảng Combo
    combos = Combo.objects.all()
    # Trả về template cùng với dữ liệu combo
    return render(request, 'comboselect/select_combo.html', {'combos': combos})

from .models import BinhLuan
from .forms import BinhLuanForm

# Hiển thị danh sách bình luận
def danh_sach_binh_luan(request):
    binh_luans = BinhLuan.objects.all()
    return render(request, 'base/danh_sach_binh_luan.html', {'binh_luans': binh_luans})

# Thêm bình luận mới
def them_binh_luan(request):
    if request.method == 'POST':
        form = BinhLuanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_binh_luan')
    else:
        form = BinhLuanForm()
    return render(request, 'base/them_binh_luan.html', {'form': form})

# Sửa bình luận
def sua_binh_luan(request, id):
    binh_luan = get_object_or_404(BinhLuan, id=id)
    if request.method == 'POST':
        form = BinhLuanForm(request.POST, instance=binh_luan)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_binh_luan')
    else:
        form = BinhLuanForm(instance=binh_luan)
    return render(request, 'base/sua_binh_luan.html', {'form': form})

# Xóa bình luận
def xoa_binh_luan(request, id):
    binh_luan = get_object_or_404(BinhLuan, id=id)
    if request.method == 'POST':
        binh_luan.delete()
        return redirect('danh_sach_binh_luan')
    return render(request, 'base/xoa_binh_luan.html', {'binh_luan': binh_luan})
