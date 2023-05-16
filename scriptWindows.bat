cd Elementos
python main.py
del ..\fop-2.8\fop\rankin.fo
copy rankin.fo ..\fop-2.8\fop
cd ..\fop-2.8\fop
fop -fo rankin.fo -pdf rankin.pdf
cd ..\..