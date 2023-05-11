# Generated by Django 4.1.3 on 2023-05-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompraSometida', '0002_alter_comprasometida_fondos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprasometida',
            name='asignacion',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('81', '81'), ('82', '82'), ('89', '89')], default=('', ''), max_length=1000),
        ),
        migrations.AlterField(
            model_name='comprasometida',
            name='concepto',
            field=models.CharField(choices=[('1', 'Nomina'), ('2', 'Facilidades y Servicios Publicos'), ('3', 'Servicios Comprados'), ('4', 'Donativos y Subsidios'), ('5', 'Gastos de Transportacion y Substinencia'), ('6', 'Servicios Profesionales'), ('7', 'Otros Gastos'), ('8', 'Inversion en Mejoras Permanentes'), ('9', 'Amortizacion de la Deuda'), ('10', 'Materiales y Suministros'), ('11', 'Compra de Equipo'), ('12', 'Anuncios y Pautas en Medios'), ('13', 'Incentivos y Subsidios Bienestar Ciudadano'), ('14', 'Aportaciones a Entidades No Gubernamentales'), ('81', 'Asignaciones Englobadas'), ('82', 'Pareo Fondos Federales'), ('89', 'Deudas de Años Anteriores')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='comprasometida',
            name='descripcion',
            field=models.CharField(choices=[('1_1110', 'Sueldos Puestos Regulares'), ('1_1111', 'Sueldo Regular  Jueces'), ('1_1112', 'Liquidacion Vacaciones Separacion Servicios'), ('1_1113', 'Pago Retroactivo Sueldo Regular'), ('1_1114', 'Sueldos Puestos de Confianza'), ('1_1115', 'Liquidacion Vacaciones Separacion Servicios  Jueces'), ('1_1120', 'Sueldos  Puestos Transitorios'), ('1_1130', 'Salarios  Personal Irregular'), ('1_1142', 'Dietas  Legisladores y Miembros de Junta'), ('1_1145', 'Honorarios a Jurados'), ('1_1160', 'Sueldos  Puestos Regulares o Transitorios Jornada Parcial '), ('1_1170', 'Sueldos  Compensacion Extraordinaria  Puestos Regulares'), ('1_1175', 'Horas Extras Task Force'), ('1_1176', 'Diferencial Task Force'), ('1_1180', 'Sueldos Compensacion Extraordinaria Puestos Transitorios'), ('1_1190', 'Salarios Compensacion Extraordinaria Puestos Irregulares'), ('1_1191', 'Pago Horas Extras Empleado de Confianza'), ('1_1195', 'Pago Incen. Econ. Renuncias Volun'), ('1_1390', 'Honorarios y Otras Compensaciones No Clasificadas '), ('1_1410', 'Comp Adic Emp Reg Bono Nav'), ('1_1412', 'Comp Adic Emp Trans Bono Nav'), ('1_1414', 'Comp Adic Emp Irreg Bono Nav'), ('1_1415', 'Bono Navidad Puestos Confianza'), ('1_1420', 'Compens Adic A Emp Subvencion'), ('1_1422', 'Gastos de Dieta por Tiempo Extra Trabajado'), ('1_1430', 'Compes A Empl Lic Enf Acumula'), ('1_1431', 'Liquidacion Exceso Licencia Enfermedad'), ('1_1432', 'Liquidacion Exceso Vacaciones'), ('1_1435', 'Liquidacion Exceso Licencia Enfermedad Jueces'), ('1_1436', 'Liq. Licencia Vacaciones Ley 70'), ('1_1437', 'Liq. Licencia Enfermedad Ley 70'), ('1_1438', 'Liq. Tiempo Compensatorio Ley 70'), ('1_1440', 'Comp Adic Emp Ret Gob. Aguinal'), ('1_1441', 'Bono de Verano Pensionados'), ('1_1460', 'Compensacion Adicional Empleados Intereses Pago Retroactivo  '), ('1_1470', 'Pago Matricula Empleados Instituciones Educativas'), ('1_1480', 'Pago por Cuido Diurno'), ('1_1490', 'Compensacion Adicional a Empleados No Clasificadas'), ('1_2810', 'Seguro de Empleados Compensacion a Obreros (FSE)'), ('1_2811', 'Seg de Emp Compensacion IRR'), ('1_2855', 'Planes Medicos Ley 70'), ('1_2870', 'Seguro de Hospital Atencion Medica a Empleados'), ('2_6010', 'Pagos por Incapacidad o Muerte'), ('2_6019', 'Pago Anual Medicamentos Pensionados'), ('2_6020', 'Pensiones A Empleados'), ('2_6021', 'Anualidad Empleados Ley 70'), ('2_6022', 'Pago Aporte Patronales Ley 70'), ('2_6030', 'Pens A Herederos o Fam De Empl'), ('2_6040', 'Adelanto de Pensiones'), ('2_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente Gastos de Funcionamiento '), ('2_6340', 'Compensaciones a Obreros y Empleados por Accidentes y Enfermedad (SSC)'), ('2_6410', 'Contribucion al Seguro Social Federal'), ('2_6411', 'Contribucion Seg. Social IRR'), ('2_6420', 'Contribucion al Medicare'), ('2_6430', 'Contribucion al Seguro Social Choferil'), ('2_6610', 'Donativos y Aportaciones a los Fondos de Pensiones del Gobierno Estatal Aportaciones del Ano Corriente '), ('2_6615', 'Retiro 2000'), ('2_6630', 'Donativos y Aportaciones al Fondo de Anualidades y Pensiones para Maestros'), ('2_6640', 'Retiro de la Judicatura de Puerto Rico'), ('2_6650', 'Pago de Contribucion por Desempleo'), ('2_6652', 'Pago de Deudas Contraidas en Anos Anteriores Contribucion por Desempleo'), ('2_9050', 'Anticipo De Fondos A Opes'), ('2_9760', 'Transferencia Operacional Out'), ('2_9761', 'Transferencia a un mismo Fondo'), ('2_9801', 'Transferencias de Saldos Libres'), ('2_9810', 'Correccion Gastos Anos Anterior'), ('2_2180', 'Pago de Lineas Telefonicas Dedicadas a Equipos de Computadoras'), ('2_2503', 'Pago de Servicios de Celulares y Beepers'), ('2_2505', 'Pago de Servicios de Telefono  Ano Corriente'), ('2_2507', 'Pago de Servicios de Telefono Larga Distancia  Entraosla'), ('2_2508', 'Pago de Servicios Larga Distancia  Fuera de Puerto Rico'), ('2_2510', 'Pago a la Autoridad de Energia Electrica  Ano Corriente'), ('2_2520', 'Pago Servicio Agua Potable y Alcantarillados  Ano Corriente'), ('2_2530', 'Gas'), ('2_2531', 'Desc. por Pronto PagoVoucher'), ('2_2590', 'Servicios Publicos  No Clasificados'), ('2_2593', 'Combustible y Lubricantes A.S.G.'), ('2_2595', 'Pago de Servicios de Salud que ofrece la Administracion de Servicios Medicos'), ('2_2596', 'Pago Serv. y Compras por CEAT'), ('2_2681', 'Pago Arrendamiento  A la Autoridad Edificios Publicos  Ano Corriente'), ('2_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente  Gastos de Funcionamiento '), ('2_9050', 'Anticipo De Fondos A Opes'), ('2_9760', 'Transferencia Operacional  Out'), ('2_9761', 'Transferencia a un mismo Fondo'), ('2_9801', 'Transferencias de Saldos Libres'), ('2_9810', 'Correcciones de Anos Anteriores'), ('3_1293', 'Servicios Privatizados  Pago Operacion de Instituciones'), ('3_1294', 'Servicios Privatizados  Pago por Servicios Prestados'), ('3_1450', 'Arrend. Sistemas Informacion '), ('3_2030', 'Impresos y Encuadernacion'), ('3_2033', 'Impresion de Sellos '), ('3_2040', 'Impresion de Leyes '), ('3_2112', 'Franqueo'), ('3_2140', 'Cable'), ('3_2181', 'Conservacion y Reparacion de Equipo de Computadora '), ('3_2192', 'Servicios de Comunicacion  No Clasificados'), ('3_2362', 'Transportacion Suministrada por la Oficina de Transporte '), ('3_2531', 'Desc. Por Pronto PagoVoucher'), ('3_2610', 'Arrendamiento de Terrenos y Suelos'), ('3_2620', 'Arrendamiento de Casas para Vivienda'), ('3_2632', 'Arrendamiento  otras Edificaciones y Construcciones o parte de los mismos  Por Contrato'), ('3_2640', 'Arrendamiento de Maquinas de Contabilidad'), ('3_2650', 'Arrendamiento de Otros Equipos de Oficina'), ('3_2670', 'Arrendamiento  Otros Equipos'), ('3_2690', 'Arrendamiento  No Clasificado'), ('3_2712', 'Conservacion y Reparacion Edificio por Contrato'), ('3_2720', 'Conservacion y Reparacion de Carreteras y Puentes  Por Contrato'), ('3_2732', 'Conservacion y Reparacion Otras Construcciones  Por Contrato'), ('3_2750', 'Conservacion y Reparacion de Equipo Construccion  Por Contrato'), ('3_2760', 'Conservacion y Reparacion Equipo de Oficina  Por Contrato'), ('3_2772', 'Consev Equipo Automotr Contra'), ('3_2780', 'Conservacion y Reparacion Otros Equipos  Por Contrato'), ('3_2792', 'Conservacion y Reparacion de Edificios y Otras Construcciones  No Clasificadas  Por Contrato'), ('3_2820', 'Seguro de Automoviles'), ('3_2830', 'Seguro Contra Incendios'), ('3_2840', 'Seguros Contra Huracan y Terremotos'), ('3_2880', 'Primas de Fianza de Fidelidad'), ('3_2890', 'Seguros  No Clasificados'), ('3_2930', 'Conservacion de Terrenos y Mejoras Secundarias'), ('3_2960', 'Adiestramiento a Funcionarios y Empleados Publicos'), ('3_2975', 'Adiestramiento Sistema de Informacion'), ('3_2980', 'Servicios Comprados  No Clasificados'), ('3_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente  Gastos de Funcionamiento '), ('3_9050', 'Anticipo de Fondos a Opes'), ('3_9760', 'Transferencias Operacional  Out'), ('3_9761', 'Transferencias a un mismo Fondo'), ('3_9801', 'Transferencias de Saldos Libres '), ('3_9810', 'Correcciones de Anos Anteriores'), ('4_6110', 'Aportaciones a Dependencias Federales'), ('4_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente  Gastos de Funcionamiento '), ('4_6130', 'Aportaciones a Municipios y Empresas del Gobierno con Tesoro Independiente  Desembolsos Capitalizables '), ('4_6140', 'Aportaciones a Municipios y Empresas del Gobierno con Tesoro Independiente Aumentar Capital de'), ('4_6150', 'Aportaciones a Municipios  Participacion en Contribuciones'), ('4_6185', 'Equipo Asistencia Tecnologica'), ('4_6310', 'Sentencias e indemnizaciones'), ('4_6470', 'Contribuciones'), ('4_6480', 'Pago en Sustitucion de Contribuciones'), ('4_6620', 'Donativos y Aportaciones a Fondos de Pensiones del Gobierno Estatal  para Cubrir Deficits Actuariales '), ('4_6710', 'Compensacion por Desempleo'), ('4_6730', 'Compensacion por Desempleo a Personas que Reciben Adiestramiento'), ('4_6740', 'Pago de Reclamaciones por Concepto de Seguro de Vida sobre Prestamos'), ('4_6890', 'Otros Subsidios  No Clasificados'), ('4_9050', 'Anticipo de fondos a Opes'), ('4_9760', 'Transferencia Operacional  Out'), ('4_9761', 'Transferencia a un mismo Fondo'), ('4_9801', 'Transferencias de Saldos Libres'), ('4_9810', 'Correcciones de Anos Anteriores'), ('5_2220', 'Servicios de Transportacion'), ('5_2310', 'Pasajes de Viaje en Puerto Rico'), ('5_2320', 'Gastos de Subsistencia en Puerto Rico'), ('5_2330', 'Pasajes de Viaje fuera de Puerto Rico'), ('5_2340', 'Subsistencia a Personas Viajan Fuera de Puerto Rico o que estan Destacados en el Exterior'), ('5_2350', 'Bonificaciones por Milla Recorrida'), ('5_2370', 'Transportacion y Subsistencia a Particulares'), ('5_2372', 'Transportacion y Dietas Jurado'), ('5_2380', 'Gastos de Viaje en Puerto Rico  No Clasificados'), ('5_2390', 'Gastos de Viaje Fuera de Puerto Rico  No Clasificados'), ('5_2410', 'Gastos de Transportacion y Entrega'), ('5_2460', 'Alojamiento en Puerto Rico'), ('5_2470', 'Alojamiento Fuera de Puerto Rico'), ('5_2490', 'Transportacion No Clasificados'), ('5_2531', 'Desc. por Pronto PagoVoucher'), ('5_2660', 'Arrendamiento  Equipo Automotriz'), ('5_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente  Gastos de Funcionamiento '), ('5_9050', 'Anticipo a Oficiales Pagadores Especiales'), ('5_9051', 'Anticipo a Oficiales Pagadores Especiales de Viaje'), ('5_9760', 'Transferencias Operacionales a Otros Fondos'), ('5_9761', 'Transferencia a un mismo Fondo'), ('5_9801', 'Transferencias de Saldos Libres'), ('5_9810', 'Correcciones de Anos Anteriores'), ('6_1210', 'Servicios Legales '), ('6_1220', 'Servicios Medicos'), ('6_1221', 'Gastos Medicos por Referidos'), ('6_1230', 'Servicios de Ingenieria y Arquitectura'), ('6_1240', 'Servicios de Contabilidad'), ('6_1250', 'Servicios Profesionales y Consultoria  OCALARH'), ('6_1260', 'Servicios Profesionales y Consultivos  Sistemas de Informacion'), ('6_1290', 'Servicios Profesionales y Consultoria  No Clasificados'), ('6_1291', 'Servicios Profesionales y Consultivos con Retenciones'), ('6_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente  Gastos de Funcionamiento '), ('6_9050', 'Anticipo a Oficiales Pagadores Especiales'), ('6_9760', 'Transferencias Operacionales a Otros Fondos'), ('6_9761', 'Transferencia a un mismo Fondo'), ('6_9801', 'Transferencias de Saldos Libres'), ('6_9810', 'Correcciones de Anos Anteriores'), ('7_1340', 'Compensacion a Pacientes de Hospitales, Confinados y Asilados en Instituciones Estatales '), ('7_2160', 'Servicios de Radiograma'), ('7_2210', 'Gastos de Restaurante y Hotel'), ('7_2230', 'Espectaculos Artisticos Especiales'), ('7_2290', 'Gastos de Representacion  No Clasificados'), ('7_2531', 'Desc. por Pronto PagoVoucher'), ('7_2675', 'Pago Arrendamiento Equipo con Opción a Compra'), ('7_2683', 'ReembPago Adquisicion Estruct'), ('7_2910', 'Cuotas y Subscripciones'), ('7_2915', 'Cuota Col Abogado Serv Publico'), ('7_2920', 'Cuidado de Animales'), ('7_2950', 'Servicio de Hospital'), ('7_2970', 'Otros Gastos  No Clasificados'), ('7_2990', 'Servicios Miscelaneos  No Clasificados'), ('7_3010', 'Servicios Bancarios'), ('7_3020', 'Intereses  Arrendamiento con Opcion a Compra'), ('7_4412', 'Alquiler Equipo Computadora'), ('7_4414', 'Compra de Equipo No Capitalizable'), ('7_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente  Gastos de Funcionamiento '), ('7_9010', 'Reintegro de Contribuciones  Ano Corriente'), ('7_9020', 'Reintegro de Otras Rentas  Ano Corriente'), ('7_9030', 'Reintegro de Contribuciones  Anos Anteriores'), ('7_9040', 'Reintegro de Otras Rentas  Anos Anteriores'), ('7_9050', 'Anticipo a Oficiales Pagadores Especiales'), ('7_9060', 'Otros Reintegros'), ('7_9061', 'Reint. Dep. Esp. IVU Agencia'), ('7_9070', 'Pago de OPE a Asoc. Emple. ELA'), ('7_9090', 'Pagos Efectuados por Fondos con Contabilidad Independiente (FIA)'), ('7_9091', 'Pago Prest/Ant a Unid Comps'), ('7_9210', 'Compra de Equipo, Materiales y Suministros para la Reventa'), ('7_9230', 'Prestamos Incobrables'), ('7_9410', 'Pago a Municipios de Contribuciones y Otros Fondos Cobrados'), ('7_9420', 'Pérdida en Liqui de Activos'), ('7_9550', 'Traspasos a Empresas del Gobierno con Tesoro Independiente'), ('7_9760', 'Transferencias Operacionales a Otros Fondos'), ('7_9761', 'Transferencia a un mismo Fondo'), ('7_9800', 'Transferencia de Capital'), ('7_9801', 'Transferencia a Saldos Libres'), ('7_9810', 'Correcciones de Anos Anteriores'), ('8_5030', 'Gasto Prop. Inmueble <=100,000'), ('8_5130', 'Equipo de Construccion'), ('8_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente  Gastos de Funcionamiento'), ('8_7010', 'Adquisicion de Terrenos para Gobierno ELA'), ('8_7110', 'Adquisicion de Terrenos para Carreteras Estatales'), ('8_7120', 'Adquisicion de Edificaciones Incidentales a las Carreteras Estatales'), ('8_7130', 'Adquisicion de Carreteras, Terrenos para Carreteras y Edificaciones Incidentales para Municipios'), ('8_7140', 'Prop Mueble > de 25,000'), ('8_7150', 'Construccion de Pavimentos o Carreteras por Contrato por el Gobierno de Puerto Rico'), ('8_7160', 'Construccion en Progreso'), ('8_7170', 'Obras y Arte y Tesoros Historicos'), ('8_7180', 'Gastos en Infraestructura'), ('8_7190', 'Pro. Inmueble No Clasificados'), ('8_7210', 'Adquisicion de Edificios, Adiciones y Mejoras Principales  Por Contrato para el Gobierno de Puerto Rico '), ('8_7230', 'Adquisicion de Edificios, Adiciones y Mejoras Principales  Para otras Entidades  Por Contrato'), ('8_7310', 'Adquisicion de Otras Mejoras por Contrato para el Gobierno de Puerto Rico'), ('8_7320', 'Adquisicion Otras Mejoras por Contrato para Municipios'), ('8_7330', 'Adquisicion Otras Mejoras por Contrato para Otras Entidades'), ('8_9760', 'Transferencias Operacionales a Otros Fondos'), ('8_9761', 'Transferencia a un mismo Fondo'), ('8_9762', 'Fondo de Construccion'), ('8_9763', 'Fondo de Renovacion y Reemplazo'), ('8_9050', 'Anticipo a Oficiales Pagadores Especiales'), ('8_9801', 'Transferencias de Saldos Libres'), ('8_9810', 'Correcciones de Anos Anteriores'), ('9_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente  Gastos de Funcionamiento'), ('9_8010', 'Pago Principal de Bonos'), ('9_8020', 'Bonos Refinanciados  Plica'), ('9_8040', 'Pago de Principal de Prestamos'), ('9_8110', 'Intereses sobre Bonos'), ('9_8120', 'Pago de Intereses sobre Prestamos'), ('9_8150', 'Intereses sobre Pagarés Especiales'), ('9_8160', 'Pago de Intereses  No Clasificados'), ('9_8170', 'Intereses sobre Aportaciones de Empleados a los Fondos de Retiro 8990 Pagos Relacionados Deuda Publica  No Clasificados'), ('9_8991', 'Des Fin a Corto Plazo'), ('9_8992', 'Gasto Emision Fina. a Corto Plazo'), ('9_9760', 'Transferencias Operacionales a Otros Fondos'), ('9_9761', 'Transferencia a un mismo Fondo'), ('10_2531', 'Desc. Por Pronto PagoVoucher'), ('10_4012', 'Materiales y Efectos Oficina'), ('10_4101', 'Materiales y Efectos Sanitarios y de Casa'), ('10_4112', 'Drogas y Medicinas'), ('10_4122', 'Efectos Quirurgicos y dentales'), ('10_4132', 'Efectos de Laboratorios'), ('10_4141', 'Efectos Fotograficos'), ('10_4142', 'Efectos de Rayos X'), ('10_4152', 'Ropa y Materiales para Ropa'), ('10_4162', 'Alimentos'), ('10_4163', 'Gastos por servicios de Alimentos'), ('10_4172', 'Alimentos para Animales'), ('10_4180', 'Efectos Agricolas'), ('10_4190', 'Semillas'), ('10_4200', 'Insecticidas'), ('10_4212', 'Materiales de Instruccion'), ('10_4214', 'Materiales y Efectos de Seguridad'), ('10_4221', 'Compra de Articulos y Materiales Recreativos'), ('10_4232', 'Combustibles, Excepto Combustibles Para Motor'), ('10_4242', 'Combustible y Lubricacion para Motores'), ('10_4250', 'Material Fabril'), ('10_4262', 'Material Para Edificios y Construcciones'), ('10_4270', 'Materiales de Extincion'), ('10_4300', 'Herramientas Menudas'), ('10_4402', 'Piezas para Equipo Automotriz'), ('10_4410', 'Piezas para otros Equipos'), ('10_4990', 'Mat Suministr y PiezasN / Cla'), ('10_4992', 'Materiales, Suministros y Piezas  No Clasificados'), ('10_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente  Gastos de Funcionamiento '), ('10_9050', 'Anticipo de Fondos a Opes'), ('10_9760', 'Transferencias Operacionales a Otros fondos'), ('10_9761', 'Transferencia a un mismo Fondo'), ('10_9801', 'Transferencias de Saldos Libres'), ('10_9810', 'Correcciones de Anos Anteriores'), ('11_2531', 'Desc. por Pronto PagoVoucher '), ('11_5050', 'Equipo de Oficina'), ('11_5060', 'Equipo de Casa'), ('11_5070', 'Equipo de Cocina'), ('11_5080', 'Equipo Educativo y Recreativo'), ('11_5090', 'Compra de Equipo de Computadoras  Hardware y Software '), ('11_5091', 'Alquiler de Equipo de Computadoras  Hardware y Software '), ('11_5092', 'Pago de Licencias de Programas de Computadoras'), ('11_5100', 'Equipo Medico, Dental y de Laboratorio'), ('11_5121', 'Compra de Vehiculos de Motor'), ('11_5124', 'Compra Equipo Nautico y de Aeronautica'), ('11_5140', 'Equipo Agricola y de Jardineria'), ('11_5150', 'Ganado'), ('11_5162', 'Libros, Tomos de Leyes, Peliculas y Discos'), ('11_5180', 'Equipo de Lavado y de Limpieza'), ('11_5200', 'Equipo Aire Acondicionado, Agua, Luz y Fuerza'), ('11_5210', 'Equipo y Efectos de Seguridad Publica'), ('11_5220', 'Equipo de Garajes, Fabricas y Talleres'), ('11_5230', 'Equipo de Almacen y de Manejo de Materiales'), ('11_5240', 'Equipo de Imprenta, Encuadernización y de Reproduccion'), ('11_5250', 'Equipo de Comunicacion y de Radiodifusion'), ('11_5260', 'Equipo de Loteria'), ('11_5490', 'Equipo  No Clasificado'), ('11_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente  Gastos de Funcionamiento '), ('11_9050', 'Anticipo de Fondos a Opes'), ('11_9760', 'Transferencias operacionales a otros Fondos'), ('11_9761', 'Transferencias a un mismo Fondo'), ('11_9801', 'Transferencias de Saldos Libres'), ('11_9810', 'Correcciones de Anos Anteriores'), ('12_1270', 'Servicios de Publicidad'), ('12_2010', 'Anuncios y Avisos Publicos'), ('12_2020', 'Anuncios Teatros Radio y Television'), ('12_2531', 'Desc. por Pronto PagoVoucher'), ('12_2940', 'Informacion Publica e Instruccion en Teatro, Radio y Television '), ('12_9050', 'Anticipo de Fondos a Opes'), ('12_9801', 'Transferencias de Saldos Libres'), ('12_9810', 'Correcciones de Anos Anteriores'), ('13_2594', 'Pago de Primas de Salud ASES'), ('13_2985', 'Raciones Servidas Comedores'), ('13_6151', 'Aportaciones a Municipios'), ('13_6179', 'Aportaciones a Becas al Personal y/o Subsidios por Adiestramiento '), ('13_6180', 'Becas y Vales Para Estudios'), ('13_6182', 'Pago por Empleo de Verano'), ('13_6210', 'Aportaciones para Ayuda'), ('13_6220', 'Ayuda para Combatir la Pobreza Extrema'), ('13_6225', 'Incentivo Energia Verde'), ('13_6360', 'Adjud / Pag No Clas Obr /Empl Les'), ('13_6720', 'Compensacion por Seguro Agricola'), ('13_6810', 'Subsidios para el Café'), ('13_6860', 'Subsidios para Proyectos de Ganado'), ('13_6890', 'Otros Subsidios  No Clasificados'), ('13_9050', 'Anticipo de Fondos a Opes'), ('13_9760', 'Transferencias de Fondos Operacionales a Otros Fondos o Reservas Requeridas '), ('13_9801', 'Transferencias de Saldos Libres'), ('13_9810', 'Correcciones de Anos Anteriores'), ('14_6170', 'Donativos y Aportaciones a Entidades Privadas'), ('14_6190', 'Donativos y Aportaciones a Individuos Excepto Para Ayuda'), ('14_6320', 'Recompensas y Compensacion por la Captura de Criminales e Investigaciones Criminales '), ('14_6325', 'Confidencias e Inspec IVULOTO'), ('14_6332', 'Premios'), ('14_6335', 'Pago de Premios IVU LOTO'), ('14_6350', 'Compensacion por Informacion y el Arresto de Criminales de Cuello Blanco'), ('14_6370', 'Compensacion por Muerte a Herederos de Obreros y Empleados'), ('14_6390', 'Otras Compensaciones  No Clasificadas'), ('14_9050', 'Anticipo de Fondos a Opes'), ('14_9760', 'Transferencias Operacionales a Otros Fondos'), ('14_9801', 'Transferencias de Saldos Libres'), ('14_9810', 'Correcciones de Anos Anteriores'), ('81_1292', 'Subcontratos con Otras Dependencias  Fondos Federales'), ('81_6120', 'Aportaciones a Municipios y a Empresas del Gobierno con Tesoro Independiente  Gastos de Funcionamiento '), ('81_9051', 'Anticipo a Oficiales Pagadores Especiales de Viaje'), ('81_9950', 'Traspaso de Costos Indirectos al Fondo General Sobrante'), ('81_9951', 'Costos Indirectos  Fondos Federales'), ('82_99999', ''), ('89_2513', 'Pago de Servicios de Celulares y Beepers  Anos Anteriores'), ('89_2514', 'Pago de Deudas Contraidas  Impresos y Encuadernacion  Anos Anteriores '), ('89_2515', 'Pago de Deudas de Telefono  Anos Anteriores'), ('89_2516', 'Pago de Deuda Autoridad de Energia Electrica  Anos Anteriores'), ('89_2517', 'Pago por Deuda por Servicio de Agua Potable y Alcantarillados  Anos Anteriores '), ('89_2518', 'Pago Deudas AEP  Anos Anteriores'), ('89_2519', 'Deudas de Anos Anteriores  No Clasificadas'), ('89_9050', 'Anticipos a Oficiales Pagadores Especiales'), ('89_9801', 'Transferencias de Saldos Libres'), ('89_9810', 'Correcciones de Anos Anteriores')], default=('', ''), max_length=1000),
        ),
        migrations.AlterField(
            model_name='comprasometida',
            name='objeto',
            field=models.CharField(choices=[('1110', '1110'), ('1111', '1111'), ('1112', '1112'), ('1113', '1113'), ('1114', '1114'), ('1115', '1115'), ('1120', '1120'), ('1130', '1130'), ('1142', '1142'), ('1145', '1145'), ('1160', '1160'), ('1170', '1170'), ('1175', '1175'), ('1176', '1176'), ('1180', '1180'), ('1190', '1190'), ('1191', '1191'), ('1195', '1195'), ('1390', '1390'), ('1410', '1410'), ('1412', '1412'), ('1414', '1414'), ('1415', '1415'), ('1420', '1420'), ('1422', '1422'), ('1430', '1430'), ('1431', '1431'), ('1432', '1432'), ('1435', '1435'), ('1436', '1436'), ('1437', '1437'), ('1438', '1438'), ('1440', '1440'), ('1441', '1441'), ('1460', '1460'), ('1470', '1470'), ('1480', '1480'), ('1490', '1490'), ('2810', '2810'), ('2811', '2811'), ('2850', '2850'), ('2855', '2855'), ('2870', '2870'), ('6010', '6010'), ('6019', '6019'), ('6020', '6020'), ('6021', '6021'), ('6022', '6022'), ('6030', '6030'), ('6040', '6040'), ('6120', '6120'), ('6340', '6340'), ('6410', '6410'), ('6411', '6411'), ('6420', '6420'), ('6430', '6430'), ('6610', '6610'), ('6615', '6615'), ('6630', '6630'), ('6640', '6640'), ('6650', '6650'), ('6652', '6652'), ('9050', '9050'), ('9760', '9760'), ('9761', '9761'), ('9801', '9801'), ('9810', '9810'), ('2180', '2180'), ('2503', '2503'), ('2505', '2505'), ('2507', '2507'), ('2508', '2508'), ('2510', '2510'), ('2520', '2520'), ('2530', '2530'), ('2531', '2531'), ('2590', '2590'), ('2593', '2593'), ('2595', '2595'), ('2596', '2596'), ('2681', '2681'), ('6120', '6120'), ('9050', '9050'), ('9760', '9760'), ('9761', '9761'), ('9801', '9801'), ('9810', '9810'), ('1293', '1293'), ('1294', '1294'), ('1450', '1450'), ('2030', '2030'), ('2033', '2033'), ('2040', '2040'), ('2112', '2112'), ('2140', '2140'), ('2181', '2181'), ('2192', '2192'), ('2362', '2362'), ('2531', '2531'), ('2610', '2610'), ('2620', '2620'), ('2632', '2632'), ('2640', '2640'), ('2650', '2650'), ('2670', '2670'), ('2690', '2690'), ('2712', '2712'), ('2720', '2720'), ('2732', '2732'), ('2750', '2750'), ('2760', '2760'), ('2772', '2772'), ('2780', '2780'), ('2792', '2792'), ('2820', '2820'), ('2830', '2830'), ('2840', '2840'), ('2880', '2880'), ('2890', '2890'), ('2930', '2930'), ('2960', '2960'), ('2975', '2975'), ('2980', '2980'), ('6120', '6120'), ('9050', '9050'), ('9760', '9760'), ('9761', '9761'), ('9801', '9801'), ('9810', '9810'), ('6110', '6110'), ('6120', '6120'), ('6130', '6130'), ('6140', '6140'), ('6150', '6150'), ('6185', '6185'), ('6310', '6310'), ('6470', '6470'), ('6480', '6480'), ('6620', '6620'), ('6710', '6710'), ('6730', '6730'), ('6740', '6740'), ('6890', '6890'), ('9050', '9050'), ('9760', '9760'), ('9761', '9761'), ('9801', '9801'), ('9810', '9810'), ('2220', '2220'), ('2310', '2310'), ('2320', '2320'), ('2330', '2330'), ('2340', '2340'), ('2350', '2350'), ('2370', '2370'), ('2372', '2372'), ('2380', '2380'), ('2390', '2390'), ('2410', '2410'), ('2460', '2460'), ('2470', '2470'), ('2490', '2490'), ('2531', '2531'), ('2660', '2660'), ('6120', '6120'), ('9050', '9050'), ('9051', '9051'), ('9760', '9760'), ('9761', '9761'), ('9801', '9801'), ('9810', '9810'), ('1210', '1210'), ('1220', '1220'), ('1221', '1221'), ('1230', '1230'), ('1240', '1240'), ('1250', '1250'), ('1260', '1260'), ('1290', '1290'), ('1291', '1291'), ('6120', '6120'), ('9050', '9050'), ('9760', '9760'), ('9761', '9761'), ('9801', '9801'), ('9810', '9810'), ('1340', '1340'), ('2160', '2160'), ('2210', '2210'), ('2230', '2230'), ('2290', '2290'), ('2531', '2531'), ('2675', '2675'), ('2683', '2683'), ('2910', '2910'), ('2915', '2915'), ('2920', '2920'), ('2950', '2950'), ('2970', '2970'), ('2990', '2990'), ('3010', '3010'), ('3020', '3020'), ('4412', '4412'), ('4414', '4414'), ('6120', '6120'), ('9010', '9010'), ('9020', '9020'), ('9030', '9030'), ('9040', '9040'), ('9050', '9050'), ('9060', '9060'), ('9061', '9061'), ('9070', '9070'), ('9090', '9090'), ('9091', '9091'), ('9210', '9210'), ('9230', '9230'), ('9410', '9410'), ('9420', '9420'), ('9550', '9550'), ('9760', '9760'), ('9761', '9761'), ('9800', '9800'), ('9801', '9801'), ('9810', '9810'), ('5030', '5030'), ('5130', '5130'), ('6120', '6120'), ('7010', '7010'), ('7110', '7110'), ('7120', '7120'), ('7130', '7130'), ('7140', '7140'), ('7150', '7150'), ('7160', '7160'), ('7170', '7170'), ('7180', '7180'), ('7190', '7190'), ('7210', '7210'), ('7230', '7230'), ('7310', '7310'), ('7320', '7320'), ('7330', '7330'), ('9760', '9760'), ('9761', '9761'), ('9762', '9762'), ('9763', '9763'), ('9050', '9050'), ('9801', '9801'), ('9810', '9810'), ('6120', '6120'), ('8010', '8010'), ('8020', '8020'), ('8040', '8040'), ('8110', '8110'), ('8120', '8120'), ('8150', '8150'), ('8160', '8160'), ('8170', '8170'), ('8991', '8991'), ('8992', '8992'), ('9760', '9760'), ('9761', '9761'), ('2531', '2531'), ('4012', '4012'), ('4101', '4101'), ('4112', '4112'), ('4122', '4122'), ('4132', '4132'), ('4141', '4141'), ('4142', '4142'), ('4152', '4152'), ('4162', '4162'), ('4163', '4163'), ('4172', '4172'), ('4180', '4180'), ('4190', '4190'), ('4200', '4200'), ('4212', '4212'), ('4214', '4214'), ('4221', '4221'), ('4232', '4232'), ('4242', '4242'), ('4250', '4250'), ('4262', '4262'), ('4270', '4270'), ('4300', '4300'), ('4402', '4402'), ('4410', '4410'), ('4990', '4990'), ('4992', '4992'), ('6120', '6120'), ('9050', '9050'), ('9760', '9760'), ('9761', '9761'), ('9801', '9801'), ('9810', '9810'), ('2531', '2531'), ('5050', '5050'), ('5060', '5060'), ('5070', '5070'), ('5080', '5080'), ('5090', '5090'), ('5091', '5091'), ('5092', '5092'), ('5100', '5100'), ('5121', '5121'), ('5124', '5124'), ('5140', '5140'), ('5150', '5150'), ('5162', '5162'), ('5180', '5180'), ('5200', '5200'), ('5210', '5210'), ('5220', '5220'), ('5230', '5230'), ('5240', '5240'), ('5250', '5250'), ('5260', '5260'), ('5490', '5490'), ('6120', '6120'), ('9050', '9050'), ('9760', '9760'), ('9761', '9761'), ('9801', '9801'), ('9810', '9810'), ('1270', '1270'), ('2010', '2010'), ('2020', '2020'), ('2531', '2531'), ('2940', '2940'), ('9050', '9050'), ('9801', '9801'), ('9810', '9810'), ('2594', '2594'), ('2985', '2985'), ('6151', '6151'), ('6179', '6179'), ('6180', '6180'), ('6182', '6182'), ('6210', '6210'), ('6220', '6220'), ('6225', '6225'), ('6360', '6360'), ('6720', '6720'), ('6810', '6810'), ('6860', '6860'), ('6890', '6890'), ('9050', '9050'), ('9760', '9760'), ('9801', '9801'), ('9810', '9810'), ('6170', '6170'), ('6190', '6190'), ('6320', '6320'), ('6325', '6325'), ('6332', '6332'), ('6335', '6335'), ('6350', '6350'), ('6370', '6370'), ('6390', '6390'), ('9050', '9050'), ('9760', '9760'), ('9801', '9801'), ('9810', '9810'), ('1292', '1292'), ('6120', '6120'), ('9051', '9051'), ('9950', '9950'), ('9951', '9951'), ('99999', '99999'), ('2513', '2513'), ('2514', '2514'), ('2515', '2515'), ('2516', '2516'), ('2517', '2517'), ('2518', '2518'), ('2519', '2519'), ('9050', '9050'), ('9801', '9801'), ('9810', '9810')], default=('-', '-'), max_length=30),
        ),
    ]
