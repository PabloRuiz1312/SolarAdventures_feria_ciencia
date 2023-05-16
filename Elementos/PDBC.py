import pymysql
class DBJuego:

    def escribirGanadores(nombres,carPuntos):
        fichero = open("rankin.fo","w")
        fichero.write("")
        fichero.close()
        fichero = open("rankin.fo","a")
        fichero.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
        fichero.write("<fo:root xmlns:fo=\"http://www.w3.org/1999/XSL/Format\">\n")
        fichero.write("<fo:layout-master-set>\n")
        fichero.write("<fo:simple-page-master master-name=\"A5\" page-height=\"14.85cm\" page-width=\"21cm\" margin-top=\"1cm\" margin-bottom=\"1cm\" margin-left=\"2cm\" margin-right=\"2cm\">\n")
        fichero.write("<fo:region-body margin-top=\"1cm\"/>\n")
        fichero.write("<fo:region-before extent=\"3cm\"/>\n")
        fichero.write("<fo:region-after extent=\"1.5cm\"/>\n")
        fichero.write("</fo:simple-page-master>\n")
        fichero.write("</fo:layout-master-set>")
        fichero.write("<fo:page-sequence master-reference=\"A5\">\n")
        fichero.write("<fo:flow flow-name=\"xsl-region-body\">\n")
        fichero.write("<fo:block font-size=\"20pt\" font-family=\"sans-serif\" font-weight=\"bold\" line-height=\"15pt\" space-after.optimum=\"30pt\" text-align=\"center\" color=\"#EC9191\">\n")
        fichero.write("RANKIN PUNTUACIONES SOLAR ADVENTURES\n")
        fichero.write("</fo:block>\n")
        fichero.write("<fo:block font-size=\"18pt\" background-color=\"yellow\" font-family=\"sans-serif\" font-weight=\"bold\" line-height=\"15pt\" space-after.optimum=\"17pt\" text-align=\"center\">\n")
        fichero.write("1er PUESTO:"+str(nombres[0])+" con "+str(carPuntos[0])+" puntos\n")
        fichero.write("</fo:block>\n")
        fichero.write("<fo:block font-size=\"16pt\" background-color=\"#C0C0C0\" font-family=\"sans-serif\" font-weight=\"bold\" line-height=\"15pt\" space-after.optimum=\"17pt\" text-align=\"center\">\n")
        fichero.write("2o PUESTO:"+str(nombres[1])+" con "+str(carPuntos[1])+" puntos\n")
        fichero.write("</fo:block>\n")
        fichero.write("<fo:block font-size=\"14pt\" background-color=\"#CD7F32\" font-family=\"sans-serif\" font-weight=\"bold\" line-height=\"15pt\" space-after.optimum=\"17pt\" text-align=\"center\">\n")
        fichero.write("3er PUESTO:"+str(nombres[2])+" con "+str(carPuntos[2])+" puntos\n")
        fichero.write("</fo:block>\n")
        fichero.write("</fo:flow>\n")
        fichero.write("</fo:page-sequence>\n")
        fichero.write("</fo:root>")
        fichero.close()