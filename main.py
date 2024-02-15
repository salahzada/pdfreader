# # #
# # # import PyPDF2 as pypdf
# # # x=0
# # # ilk=0
# # # son=0
# # # npage=0
# # # cumle=""
# # # cumlelist=[]
# # # text=""
# # # clean1=[]
# # #
# # # pdfFileObj = open('C:\\Users\\salah\\Desktop\\bigdatadocuments\\Avtoreferat_Araz_Poladov_azərbaycan_son_çap_2-21.pdf', 'rb')
# # # reader = pypdf.PdfReader(pdfFileObj)
# # #
# # # while(npage<len(reader.pages)):
# # #     pageObj = reader.pages[npage]
# # #     clean1+=pageObj.extract_text().split("\n")
# # #     npage+=1
# # # for c in clean1:
# # #     text+=c
# # #
# # # words=text.split(" ")
# # #
# # # while("" in words):
# # #     words.remove("")
# # #
# # # def lastword(word):
# # #     if word.endswith("ir.") or word.endswith("ır.") or word.endswith("ur.") or word.endswith("ür.") or words[x].endswith("ar.") or word.endswith("ər.") or word.endswith("aq.") or word.endswith("ək."):
# # #         return True
# # #     else:
# # #         return False
# # #
# # # while (x<len(words)):
# # #     if lastword(words[x]):
# # #         son=x
# # #         while(son>=ilk):
# # #             cumle+=words[ilk]+" "
# # #             ilk+=1
# # #         cumle+="\n\n"
# # #     x += 1
# # #
# # # print(cumle)
# # #
# # # with open("text.txt","w",encoding='utf-8') as file:
# # #     file.write(cumle)
# # # pdfFileObj.close()
# #
# #
# # #------------------------------------------------------
# #
# #
# # import PyPDF2 as pypdf
# # x=0
# # ilk=0
# # son=-1
# # npage=1
# # cumle=""
# # cumlelist=[]
# # text=""
# # clean1=[]
# # # pdfFileObj = open('C:\\Users\\salah\\Desktop\\bigdatadocuments\\Avtoreferat_Araz_Poladov_azərbaycan_son_çap_2-21.pdf', 'rb')
# # # pdfFileObj = open('C:\\Users\\salah\\Desktop\\bigdatadocuments\\Avtoreferat_AZ.pdf', 'rb')
# # # pdfFileObj = open('C:\\Users\\salah\\Desktop\\bigdatadocuments\\Avtoreferat_Şahin_Azərbaycan_son.pdf', 'rb')
# # # pdfFileObj = open('C:\\Users\\salah\\Desktop\\bigdatadocuments\\Aytac_Qasımova_avtoreferat_azərbaycan_variantı_2022_ən_son_yeni_çap.pdf', 'rb')
# # # pdfFileObj = open('C:\\Users\\salah\\Desktop\\bigdatadocuments\\AZ_Avtoreferat_Firuza_Mayilova_19_09_2022.pdf', 'rb')
# # # pdfFileObj = open('C:\\Users\\salah\\Desktop\\bigdatadocuments\\Elmira_Avtoreferat_Az3.pdf', 'rb')
# # # pdfFileObj = open('C:\\Users\\salah\\Desktop\\bigdatadocuments\\Əsmər_Pənahova_azərbaycan_variantı_2022.pdf', 'rb')
# # # pdfFileObj = open('C:\\Users\\salah\\Desktop\\bigdatadocuments\\Fidan_AVTOREFERAT_AZ.pdf', 'rb')
# # # pdfFileObj = open('C:\\Users\\salah\\Desktop\\bigdatadocuments\\XƏLİLOV_F_Avtoreferat_AZƏRBAYCAN.pdf', 'rb')
# #
# # # pdfFileObj = open('C:\\Users\\salah\\Desktop\\bigdatadocuments\\Vafa_Avtoreferat_AZ.pdf', 'rb')
# #
# # reader = pypdf.PdfReader(pdfFileObj)
# # while(npage<len(reader.pages)):
# #     pageObj = reader.pages[npage]
# #     clean1+=pageObj.extract_text().split("\n")
# #     npage+=1
# # for c in clean1:
# #     text+=c
# # words=text.split(" ")
# #
# # while("" in words):
# #     words.remove("")
# # for m in words:
# #     if m.startswith("ə"):
# #         index=words.index(m)
# #         words[index-1]+=words[index]
# #         words.remove(words[index])
# # def lastword(word):
# #     if word.endswith("ir.") or word.endswith("ır.") or word.endswith("ur.") or word.endswith("ür.") or words[x].endswith("ar.") or word.endswith("ər.") or word.endswith("aq.") or word.endswith("ək."):
# #         return True
# #     else:
# #         return False
# # while (x<len(words)):
# #     ilk = son + 1
# #     if lastword(words[x]):
# #         son=x
# #         while(son>=ilk):
# #
# #             cumle+=words[ilk]+" "
# #             ilk+=1
# #         cumle+="\n\n"
# #     x += 1
# # # print(cumle)
# #
# # # with open("11032022-law-elchin-salahzada(vafa).txt","w",encoding='utf-8') as file:
# #
# # # with open("24112022-law-elchin-salahzada.txt","w",encoding='utf-8') as file:
# # # with open("11032022-law-elchin-salahzada.txt","w",encoding='utf-8') as file:
# # # with open("31012022-law-elchin-salahzada(esmer).txt","w",encoding='utf-8') as file:
# # # with open("30062022-law-elchin-salahzada.txt","w",encoding='utf-8') as file:
# # # with open("28102022-law-elchin-salahzada.txt","w",encoding='utf-8') as file:
# # # with open("23122022-law-elchin-salahzada(aytac).txt","w",encoding='utf-8') as file:
# # # with open("31012022-law-elchin-salahzada.txt","w",encoding='utf-8') as file:
# # # with open("23122021-law-elchin-salahzada.txt","w",encoding='utf-8') as file:
# # # with open("23122022-law-elchin-salahzada(vuqaraftoaz).txt","w",encoding='utf-8') as file:
# #     file.write(cumle)
# # pdfFileObj.close()
#
# #--------------------------------------------------------------------------------
# from tkinter import *
# # renglerin verilmesi: rgb (red,green, blue), hex (hexadecimal value), color name (rengin adi)
# count=16777215
# #16777215 limit
#
# def test():
#     global count
#     count-=20
#     b.configure(bg=f'#{str(hex(count)).split("x")[1]}')
# root=Tk()
#
# b=Button(text="click", command=test)
# b.pack()
# root.mainloop()




