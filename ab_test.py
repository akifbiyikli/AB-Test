import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# İş Problemi
# Facebook kısa süre önce mevcut maximum bidding adı verilen teklif
# verme türüne alternatif olarak yeni bir teklif türü olan average bidding’i
# tanıttı.
# Müşterilerimizden biri olan bombabomba.com, bu yeni özelliği test
# etmeye karar verdi ve averagebidding’in, maximumbidding’den daha
# fazla dönüşüm getirip getirmediğini anlamak için bir A/B testi yapmak
# istiyor.
# Maximum Bidding: Maksimum teklif verme
# Average Bidding: Average teklif verme

# Veri Seti Hikayesi
# bombabomba.com’un web site bilgilerini içeren bu veri setinde kullanıcıların
# gördükleri ve tıkladıkları reklam sayıları gibi bilgilerin yanı sıra buradan gelen
# kazanç bilgileri yer almaktadır.
# Kontrol ve Test grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleri
# ab_testing.xlsx excelinin ayrı sayfalarında yer almaktadır.

# Impression – Reklam görüntüleme sayısı
# Click – Tıklama
# Görüntülenen reklama tıklanma sayısını belirtir.
# Değişkenler
# Purchase – Satın alım
# Tıklanan reklamlar sonrası satın alınan ürün sayısını belirtir.
# Earning – Kazanç
# Satın alınan ürünler sonrası elde edilen kazanç




# Görev 1:
# A/B testinin hipotezini tanımlayınız.

#H0: Control ve Test Grouplarının ortalaması  arasında fark yoktur.
#H1: ... vardır.

# Descriptive Statistics (Betimsel İstatistikler)


ctrl_group = pd.read_excel("datasets/ab_testing.xlsx", sheet_name= "Control Group")
test_group = pd.read_excel("datasets/ab_testing.xlsx", sheet_name= "Test Group")
ctrl_group.describe().T
test_group.describe().T

ctrl_group.isnull().sum()
test_group.isnull().sum()
ctrl_group["Purchase"].mean()
test_group["Purchase"].mean()



# Varsayım sağlanıyorsa pearson sağlanmıyorsa Spearman.

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.

test_stat, pvalue = shapiro(ctrl_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(test_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# H0 reddedilemez. p-value > 0.05(p-value(ctrl) = 0.5891, p-value(test) = 0.1541). Dağılımlar Normaldir.

# Varyans homojenliği
# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir
test_stat, pvalue = levene(ctrl_group["Purchase"],
                           test_group["Purchase"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# H0 reddilemez. p-value >0.05(p-value = 0.1083). Varyanslar Homojendir.

# Görev 2:
# Hipotez testini gerçekleştiriniz. Çıkan
# sonuçların istatistiksel olarak anlamlı olup
# olmadığını yorumlayınız.
test_stat, pvalue = ttest_ind(ctrl_group["Purchase"],
                              test_group["Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0 reddedilemez(p-value = 0.3493). Ortalamalar arasında istatistiksel olarak anlamlı bir fark yoktur.



# Görev 3:
# Hangi testi kullandınız, sebeplerini belirtiniz.

# Normallik dağılım testi için shapiro-wilks testi yaptık. Dağılımlar normal dağılıyor.
# Varyans homojenliğini levene ile  test ettik. varyanslar homojendir.
# Varsayımlarımız sağlandığı için Bağımsız İki Örneklem T-test'ini uyguladık. Varyansların homojen dağıldığını da belirttik.



# Görev 4:
# Görev 2’de verdiğiniz cevaba göre, müşteriye
# tavsiyeniz nedir?

# iki uygulama arasında fark yoktur. Kontrol ve Test gruplarının sayısı 40'ar olduğu için deneyin sürdürülüp daha fazla katılımcı ile gerçekleştirilmesini öneririm.




