@echo off
echo Python ortamini kontrol ediyorum...
python --version
if %errorlevel% neq 0 (
    echo Python bulunamadi. Lutfen Python'u yukleyin ve PATH seçeneğini seçin.
    exit /b
)

echo Gerekli kutuphaneleri yuklemek icin pip kullaniliyor...
pip install psutil
pip install time
pip install signal
pip install sys
echo Tum kutuphaneler basariyla yuklendi.
pause

