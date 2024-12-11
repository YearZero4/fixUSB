import psutil, time, subprocess, shutil, os

script = __file__
nscript=os.path.basename(script)
user = os.getlogin()
folder = 'script_home'
rshome=f'C:\\Users\\{user}\\AppData\\{folder}'
rcopy=f"{rshome}\\{nscript}"

if not os.path.exists(rshome):
 os.makedirs(rshome)
if not os.path.exists(rcopy):
 shutil.copy(script, rcopy)

os.system(f'reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v fixUSB /t REG_SZ /d {rcopy} /f >nul 2>nul')

unidades_analizadas = set()

while True:
 from tkinter import messagebox
 x = psutil.disk_partitions()
 unidades_actuales = {unidad.device[:-1] for unidad in x if 'rw,removable' in unidad.opts}
 for unidad in unidades_actuales:
  if unidad not in unidades_analizadas:
   messagebox.showinfo(f"ANALISIS", f"UNIDAD {unidad} ENCONTRDA,\nVERIFICANDO. POR FAVOR ESPERE")
   unidades_analizadas.add(unidad)
   command = f'chkdsk /f {unidad}'
   exk=subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
   if exk.stdout:
    messagebox.showinfo(f"ANALISIS", f"UNIDAD {unidad} VERIFICADA EXITOSAMENTE\nESTA LISTA PARA USARSE")
                

 unidades_analizadas = {unidad for unidad in unidades_analizadas if unidad in unidades_actuales}
 time.sleep(1)