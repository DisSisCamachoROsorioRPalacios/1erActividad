from Login import Login
from Servidor import Servidor
print('---Login---\n')
log=Login();
log.ObtenerUsuario();
log.ObtenerContra();
ser=Servidor()
ser.VerificarDatos(log.getUsuario(),log.getContra())
