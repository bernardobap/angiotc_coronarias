from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import date
import csv
import sys
import os

root = Tk()
root.title("Formulario Angiotomografia de Coronarias")

medicos = ('Doc1', 'Doc2', 'Doc3', 'Doc4', 'Doc5', 'Doc6')
etnias = ('Branco', 'Negro', 'Hispanico', 'Chines')

# Variável do checkbox para controle de entrada no campo ec (escore de cálcio)
ec_nan = BooleanVar()

# Variáveis de entrada
num_acesso = StringVar()
idade = IntVar()
etnia = StringVar()     
peso = IntVar()
altura = IntVar()
sexo = IntVar()
origem = IntVar()
indicacao = IntVar()
fr_has = IntVar()
fr_dlp = IntVar()
fr_tbg = IntVar()
fr_sedent = IntVar()
fr_dm = IntVar()
fr_iam = IntVar()
fr_dac = IntVar()
fr_equiv_dac = IntVar()
stent = IntVar()
rm = IntVar()
ic = IntVar()
a_vent = IntVar()
tpsv = IntVar()
fa = IntVar()
hf_dac = IntVar()
tipo_dor = IntVar()
bbloq = IntVar()
iecabra = IntVar()
bcc = IntVar()
tiazidico = IntVar()
espironolactona = IntVar()
furosemida = IntVar()
nitrato = IntVar()
hidralazina = IntVar()
estatina = IntVar()
aas = IntVar()
p2y12 = IntVar()
te = IntVar()
cintilo = IntVar()
ecoestresse = IntVar()
cate = IntVar()
ec = IntVar()
dominancia = IntVar()
tce = IntVar()
dap = IntVar()
dam = IntVar()
dad = IntVar()
dg = IntVar()
ri = IntVar()
cxp = IntVar()
cxd = IntVar()
mg = IntVar()
cdp = IntVar()
cdm = IntVar()
cdd = IntVar()
dp = IntVar()
vp = IntVar()
stent_tce = IntVar()
stent_da = IntVar()
stent_dg = IntVar()
stent_cx = IntVar()
stent_mg = IntVar()
stent_cd = IntVar()
stent_dp = IntVar()
stent_vp = IntVar()
atie = IntVar()
atid = IntVar()
evasc = IntVar()
rm_da = IntVar()
rm_dg = IntVar()
rm_mg = IntVar()
rm_cd = IntVar()
rm_dp = IntVar()
obs = StringVar()
laudado_por = StringVar()
data = StringVar()


def gerar_frame_stent():
    stent_f = ttk.Labelframe(root, text='Stent:')
    stent_legenda = Message(
        stent_f, text='0) Ausente\n1) Pérvio\n2) Reestenose\n' +
        '3) Ocluído\n4) Não avaliável', justify=LEFT)
    stent_tce_l = ttk.Label(stent_f, text='TCE: ')
    stent_tce_scale = Scale(stent_f, from_=0, to=4, resolution=1,
                            orient=HORIZONTAL, variable=stent_tce)
    stent_da_l = ttk.Label(stent_f, text='DA: ')
    stent_da_scale = Scale(stent_f, from_=0, to=4, resolution=1,
                           orient=HORIZONTAL, variable=stent_da)
    stent_dg_l = ttk.Label(stent_f, text='DG: ')
    stent_dg_scale = Scale(stent_f, from_=0, to=4, resolution=1,
                           orient=HORIZONTAL, variable=stent_dg)
    stent_cx_l = ttk.Label(stent_f, text='CX: ')
    stent_cx_scale = Scale(stent_f, from_=0, to=4, resolution=1,
                           orient=HORIZONTAL, variable=stent_cx)
    stent_mg_l = ttk.Label(stent_f, text='MG: ')
    stent_mg_scale = Scale(stent_f, from_=0, to=4, resolution=1,
                           orient=HORIZONTAL, variable=stent_mg)
    stent_cd_l = ttk.Label(stent_f, text='CD: ')
    stent_cd_scale = Scale(stent_f, from_=0, to=4, resolution=1,
                           orient=HORIZONTAL, variable=stent_cd)
    stent_dp_l = ttk.Label(stent_f, text='DP: ')
    stent_dp_scale = Scale(stent_f, from_=0, to=4, resolution=1,
                           orient=HORIZONTAL, variable=stent_dp)
    stent_vp_l = ttk.Label(stent_f, text='VP: ')
    stent_vp_scale = Scale(stent_f, from_=0, to=4, resolution=1,
                           orient=HORIZONTAL, variable=stent_vp)

    stent_f.grid(row=2, column=6, padx=5, pady=5, sticky=N)
    stent_tce_l.grid(row=1, column=0, sticky=W + S)
    stent_tce_scale.grid(row=1, column=1)
    stent_da_l.grid(row=2, column=0, sticky=W + S)
    stent_da_scale.grid(row=2, column=1)
    stent_dg_l.grid(row=3, column=0, sticky=W + S)
    stent_dg_scale.grid(row=3, column=1)
    stent_cx_l.grid(row=4, column=0, sticky=W + S)
    stent_cx_scale.grid(row=4, column=1)
    stent_mg_l.grid(row=5, column=0, sticky=W + S)
    stent_mg_scale.grid(row=5, column=1)
    stent_cd_l.grid(row=6, column=0, sticky=W + S)
    stent_cd_scale.grid(row=6, column=1)
    stent_dp_l.grid(row=7, column=0, sticky=W + S)
    stent_dp_scale.grid(row=7, column=1)
    stent_vp_l.grid(row=8, column=0, sticky=W + S)
    stent_vp_scale.grid(row=8, column=1)
    stent_legenda.grid(row=9, column=0, columnspan=2, sticky=W, pady=6)


def gerar_frame_rm():
    rm_f = ttk.Labelframe(root, text='RM Cirúrgica:')
    rm_legenda = Message(
        rm_f, text='0) Ausente\n1) Sem placa\n2) <50%\n3) >50%\n4) Ocluído',
        justify=LEFT)
    rm_tipos_l = ttk.Label(rm_f, text='Tipos:')
    rm_atie = ttk.Checkbutton(rm_f, text='ATIE', variable=atie)
    rm_atid = ttk.Checkbutton(rm_f, text='ATID', variable=atid)
    rm_evasc = ttk.Checkbutton(rm_f, text='Enxerto vascular', variable=evasc)
    rm_da_l = ttk.Label(rm_f, text='para DA:')
    rm_da_scale = Scale(rm_f, from_=0, to=4, resolution=1,
                        orient=HORIZONTAL, variable=rm_da)
    rm_dg_l = ttk.Label(rm_f, text='para DG: ')
    rm_dg_scale = Scale(rm_f, from_=0, to=4, resolution=1,
                        orient=HORIZONTAL, variable=rm_dg)
    rm_mg_l = ttk.Label(rm_f, text='para MG: ')
    rm_mg_scale = Scale(rm_f, from_=0, to=4, resolution=1,
                        orient=HORIZONTAL, variable=rm_mg)
    rm_cd_l = ttk.Label(rm_f, text='para CD: ')
    rm_cd_scale = Scale(rm_f, from_=0, to=4, resolution=1,
                        orient=HORIZONTAL, variable=rm_cd)
    rm_dp_l = ttk.Label(rm_f, text='para DP: ')
    rm_dp_scale = Scale(rm_f, from_=0, to=4, resolution=1,
                        orient=HORIZONTAL, variable=rm_dp)

    rm_f.grid(row=2, column=7, padx=5, pady=5, sticky=N)
    rm_tipos_l.grid(row=1, column=0, columnspan=2, sticky=W)
    rm_atie.grid(row=2, column=0, columnspan=2, sticky=W)
    rm_atid.grid(row=3, column=0, columnspan=2, sticky=W)
    rm_evasc.grid(row=4, column=0, columnspan=2, sticky=W)
    rm_da_l.grid(row=5, column=0, sticky=W + S)
    rm_da_scale.grid(row=5, column=1)
    rm_dg_l.grid(row=6, column=0, sticky=W + S)
    rm_dg_scale.grid(row=6, column=1)
    rm_mg_l.grid(row=7, column=0, sticky=W + S)
    rm_mg_scale.grid(row=7, column=1)
    rm_cd_l.grid(row=8, column=0, sticky=W + S)
    rm_cd_scale.grid(row=8, column=1)
    rm_dp_l.grid(row=9, column=0, sticky=W + S)
    rm_dp_scale.grid(row=9, column=1)
    rm_legenda.grid(row=10, column=0, columnspan=2, sticky=W, pady=6)


def trocar(seg):
    valor = seg.get()
    if 0 <= valor <= 5:
        seg.set((seg.get() + 1) % 6)


def controle_ec():
    if ec_nan.get():
        ec_e.config(state='disabled')
        ec.set(float('nan'))
    else:
        ec_e.config(state='normal')


def submeter():
    try:
        dados = {
            'num_acesso': num_acesso.get(),
            'idade': idade.get(),
            'etnia': etnia.get(),
            'peso': peso.get(),
            'altura': altura.get(),
            'sexo': sexo.get(),
            'origem': origem.get(),
	        'indicacao': indicacao.get(),	
            'fr_has': fr_has.get(),
            'fr_dlp': fr_dlp.get(),
            'fr_tbg': fr_tbg.get(),
            'fr_sedent': fr_sedent.get(),
            'fr_dm': fr_dm.get(),
            'fr_iam': fr_iam.get(),
            'fr_dac': fr_dac.get(),
            'fr_equiv_dac': fr_equiv_dac.get(),
            'stent': stent.get(),
            'rm': rm.get(),
            'ic': ic.get(),
            'a_vent': a_vent.get(),
            'tpsv': tpsv.get(),
            'fa': fa.get(),
            'hf_dac': hf_dac.get(),
            'tipo_dor': tipo_dor.get(),
            'bbloq': bbloq.get(),
            'iecabra': iecabra.get(),
            'bcc': bcc.get(),
            'tiazidico': tiazidico.get(),
            'espironolactona': espironolactona.get(),
            'furosemida': furosemida.get(),
            'nitrato': nitrato.get(),
            'hidralazina': hidralazina.get(),
            'estatina': estatina.get(),
            'aas': aas.get(),
            'p2y12': p2y12.get(),
            'te': te.get(),
            'cintilo': cintilo.get(),
            'ecoestresse': ecoestresse.get(),
            'cate': cate.get(),
            'ec': ec.get(),
            'dominancia': dominancia.get(),
            'tce': tce.get(),
            'dap': dap.get(),
            'dam': dam.get(),
            'dad': dad.get(),
            'dg': dg.get(),
            'ri': ri.get(),
            'cxp': cxp.get(),
            'cxd': cxd.get(),
            'mg': mg.get(),
            'cdp': cdp.get(),
            'cdm': cdm.get(),
            'cdd': cdd.get(),
            'dp': dp.get(),
            'vp': vp.get(),
            'stent_tce': stent_tce.get(),
            'stent_da': stent_da.get(),
            'stent_dg': stent_dg.get(),
            'stent_cx': stent_cx.get(),
            'stent_mg': stent_mg.get(),
            'stent_cd': stent_cd.get(),
            'stent_dp': stent_dp.get(),
            'stent_vp': stent_vp.get(),
            'atie': atie.get(),
            'atid': atid.get(),
            'evasc': evasc.get(),
            'rm_da': rm_da.get(),
            'rm_dg': rm_dg.get(),
            'rm_mg': rm_mg.get(),
            'rm_cd': rm_cd.get(),
            'rm_dp': rm_dp.get(), 
            'laudado_por': laudado_por.get(),
            'data': data.get(),
            'obs': obs.get(),
        }
        with open('tab_coronaria.csv', 'a') as csvfile:
            fieldnames = [
                'num_acesso',
                'idade',
                'etnia',
                'peso',
                'altura',
                'sexo',
                'origem',
		'indicacao',
                'fr_has',
                'fr_dlp',
                'fr_tbg',
                'fr_sedent',
                'fr_dm',
                'fr_iam',
                'fr_dac',
                'fr_equiv_dac',
                'stent',
                'rm',
                'ic',
                'a_vent',
                'tpsv',
                'fa',
                'hf_dac',
                'tipo_dor',
                'bbloq',
                'iecabra',
                'bcc',
                'tiazidico',
                'espironolactona',
                'furosemida',
                'nitrato',
                'hidralazina',
                'estatina',
                'aas',
                'p2y12',
                'te',
                'cintilo',
                'ecoestresse',
                'cate',
                'ec',
                'dominancia',
                'tce',
                'dap',
                'dam',
                'dad',
                'dg',
                'ri',
                'cxp',
                'cxd',
                'mg',
                'cdp',
                'cdm',
                'cdd',
                'dp',
                'vp',
                'stent_tce',
                'stent_da',
                'stent_dg',
                'stent_cx',
                'stent_mg',
                'stent_cd',
                'stent_dp',
                'stent_vp',
                'atie',
                'atid',
                'evasc',
                'rm_da',
                'rm_dg',
                'rm_mg',
                'rm_cd',
                'rm_dp',
                'laudado_por',
                'data',
                'obs',
            ]
            writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writerow(dados)
    except TclError:
        messagebox.showinfo(message='Reveja as informações inseridas!',
                            title='Erro', icon='error')


def validar():
    if etnia.get() == '':
        messagebox.showinfo(message='Insira a etnia!',
                            title='Erro', icon='error')
    elif not num_acesso.get().isdigit():
        messagebox.showinfo(message='Insira um número de acesso válido!',
                            title='Erro', icon='error')
    elif not (laudado_por.get() in medicos):
        messagebox.showinfo(message='Insira o médico responsável!',
                            title='Erro', icon='error')
    elif idade.get() <= 10 or idade.get() > 130:
        messagebox.showinfo(message='Insira uma idade válida!',
                            title='Erro', icon='error')
    elif peso.get() <= 30 or peso.get() > 200:
        messagebox.showinfo(message='Insira um peso válido e em kg!',
                            title='Erro', icon='error')
    elif altura.get() <= 100 or peso.get() > 250:
        messagebox.showinfo(message='Insira uma altura válida e em cm!',
                            title='Erro', icon='error')
    else:
        confirma_submeter = messagebox.askyesno(
            message='Confirma a inclusão?', title='Confirmação')
        if confirma_submeter:
            submeter()
        else:
            pass


def limpar_janela():
    confirma_limpar = messagebox.askyesno(
        message='Quer mesmo limpar os campos?', title='Confirmação')
    if confirma_limpar:
        restart()
    else:
        pass


def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)


# Dados paciente
dados_f = ttk.Labelframe(root, text='Dados do Paciente:')
num_acesso_l = ttk.Label(dados_f, text='Num Acesso: ')
num_acesso_e = ttk.Entry(dados_f, textvariable=num_acesso, width=12)
sep3 = ttk.Separator(dados_f, orient=HORIZONTAL)
idade_l = ttk.Label(dados_f, text='Idade:')
idade_e = ttk.Entry(dados_f, textvariable=idade, width=5)
etnia_l = ttk.Label(dados_f, text='Etnia:')
etnia_combob = ttk.Combobox(dados_f, textvariable=etnia, values=etnias,
                            width=10)
peso_l = ttk.Label(dados_f, text='Peso(kg):')
peso_e = ttk.Entry(dados_f, textvariable=peso, width=5)
altura_l = ttk.Label(dados_f, text='Altura(cm):')
altura_e = ttk.Entry(dados_f, textvariable=altura, width=5)
sexo_l = ttk.Label(dados_f, text='Sexo:')
sexo_m_rb = ttk.Radiobutton(dados_f, text='M', variable=sexo, value=1)
sexo_f_rb = ttk.Radiobutton(dados_f, text='F', variable=sexo, value=0)
sep6 = ttk.Separator(dados_f, orient=HORIZONTAL)
origem_l = ttk.Label(dados_f, text='Origem: ')
origem_rb1 = ttk.Radiobutton(dados_f, text='Eletivo', variable=origem, value=0)
origem_rb2 = ttk.Radiobutton(dados_f, text='PS/internado',
                             variable=origem, value=1)
sep7 = ttk.Separator(dados_f, orient=HORIZONTAL)
indicacao_l = ttk.Label(dados_f, text='Indicação: ')
indicacao_rb1 = ttk.Radiobutton(dados_f, text='Suspeita de DAC', variable=indicacao, value=0)
indicacao_rb2 = ttk.Radiobutton(dados_f, text='DAC conhecida', variable=indicacao, value=1)
indicacao_rb3 = ttk.Radiobutton(dados_f, text='Suspeita de SCA', variable=indicacao, value=2)
indicacao_rb4 = ttk.Radiobutton(dados_f, text='Suspeita de Miocardite', variable=indicacao, value=3)
indicacao_rb5 = ttk.Radiobutton(dados_f, text='Pré operatório', variable=indicacao, value=4)
indicacao_rb6 = ttk.Radiobutton(dados_f, text='Anomalia coronariana', variable=indicacao, value=5)

# Antecedentes
antec_f = ttk.Labelframe(root, text='Antecedentes:')
has_cb = ttk.Checkbutton(antec_f, text='HAS', variable=fr_has)
dlp_cb = ttk.Checkbutton(antec_f, text='DLP', variable=fr_dlp)
tbg_cb = ttk.Checkbutton(antec_f, text='TBG', variable=fr_tbg)
sedent_cb = ttk.Checkbutton(antec_f, text='Sedentarismo', variable=fr_sedent)
dm_cb = ttk.Checkbutton(antec_f, text='DM', variable=fr_dm)
iam_cb = ttk.Checkbutton(antec_f, text='IAM prévio', variable=fr_iam)
dac_cb = ttk.Checkbutton(antec_f, text='DAC conhecida', variable=fr_dac)
equiv_dac_cb = ttk.Checkbutton(antec_f, text='Equivalente DAC',
                               variable=fr_equiv_dac)
stent_cb = ttk.Checkbutton(antec_f, text='Stent', variable=stent,
                           command=gerar_frame_stent)
rm_cb = ttk.Checkbutton(antec_f, text='RM cirúrgica', variable=rm,
                        command=gerar_frame_rm)
ic_cb = ttk.Checkbutton(antec_f, text='IC', variable=ic)
a_vent_cb = ttk.Checkbutton(antec_f, text='Arrit. ventricular',
                            variable=a_vent)
fa_cb = ttk.Checkbutton(antec_f, text='FA/flutter', variable=fa)
tpsv_cb = ttk.Checkbutton(antec_f, text='TPSV', variable=tpsv)
hf_dac_cb = ttk.Checkbutton(antec_f, text='HF DAC precoce', variable=hf_dac)

# Clínica
clinica_f = ttk.Labelframe(root, text='Clínica:')
tipica_rb = ttk.Radiobutton(clinica_f, text='Angina típica',
                            variable=tipo_dor, value=4)
p_anginosa_rb = ttk.Radiobutton(
    clinica_f, text='Provavelmente anginosa', variable=tipo_dor, value=3)
p_n_anginosa_rb = ttk.Radiobutton(
    clinica_f, text='Provavemente não anginosa', variable=tipo_dor, value=2)
equiv_anginoso_rb = ttk.Radiobutton(
    clinica_f, text='Equivalente anginoso', variable=tipo_dor, value=1)
assint_rb = ttk.Radiobutton(clinica_f, text='Assintomático',
                            variable=tipo_dor, value=0)

# Medicamentos
medicamentos_f = ttk.Labelframe(root, text='Medicamentos:')
bbloq_cb = ttk.Checkbutton(medicamentos_f, text='Beta-bloqueador',
                           variable=bbloq)
iecabra_cb = ttk.Checkbutton(medicamentos_f, text='IECA/BRA', variable=iecabra)
bcc_cb = ttk.Checkbutton(medicamentos_f, text='Bloq canal Ca', variable=bcc)
tiaz_cb = ttk.Checkbutton(medicamentos_f, text='Tiazidico', variable=tiazidico)
espirono_cb = ttk.Checkbutton(medicamentos_f, text='Espironolactona',
                              variable=espironolactona)
furo_cb = ttk.Checkbutton(medicamentos_f, text='Furosemida',
                          variable=furosemida)
nitrato_cb = ttk.Checkbutton(medicamentos_f, text='Nitrato', variable=nitrato)
hdz_cb = ttk.Checkbutton(medicamentos_f, text='Hidralazina',
                         variable=hidralazina)
estatina_cb = ttk.Checkbutton(medicamentos_f, text='Estatina',
                              variable=estatina)
aas_cb = ttk.Checkbutton(medicamentos_f, text='AAS', variable=aas)
p2y12_cb = ttk.Checkbutton(medicamentos_f, text='Inibidores P2Y12',
                           variable=p2y12)

# Exames prévios
exames_f = ttk.Labelframe(root, text='Exames prévios:')
te_l = Label(exames_f, text='TE:')
te_nao_rb = ttk.Radiobutton(exames_f, text='não', variable=te, value=0)
te_ineficaz_rb = ttk.Radiobutton(exames_f, text='ineficaz', variable=te,
                                 value=1)
te_neg_rb = ttk.Radiobutton(exames_f, text='negativo', variable=te, value=2)
te_pos_rb = ttk.Radiobutton(exames_f, text='positivo', variable=te, value=3)
sep1 = ttk.Separator(exames_f, orient=HORIZONTAL)
cintilo_l = Label(exames_f, text='Cintilografia:')
cintilo_nao_rb = ttk.Radiobutton(exames_f, text='não',
                                 variable=cintilo, value=0)
cintilo_neg_rb = ttk.Radiobutton(exames_f, text='negativa',
                                 variable=cintilo, value=1)
cintilo_pos1_rb = ttk.Radiobutton(exames_f, text='positiva discreta',
                                  variable=cintilo, value=2)
cintilo_pos2_rb = ttk.Radiobutton(exames_f, text='positiva mod/imp',
                                  variable=cintilo, value=3)
sep2 = ttk.Separator(exames_f, orient=HORIZONTAL)
eco_l = Label(exames_f, text='ECO estresse:')
eco_nao_rb = ttk.Radiobutton(exames_f, text='não',
                             variable=ecoestresse, value=0)
eco_neg_rb = ttk.Radiobutton(exames_f, text='negativo',
                             variable=ecoestresse, value=1)
eco_pos1_rb = ttk.Radiobutton(exames_f, text='positivo discreto',
                              variable=ecoestresse, value=2)
eco_pos2_rb = ttk.Radiobutton(exames_f, text='positivo mod/imp',
                              variable=ecoestresse, value=3)
sep5 = ttk.Separator(exames_f, orient=HORIZONTAL)
cate_l = Label(exames_f, text='CATE:')
cate_nao_rb = ttk.Radiobutton(exames_f, text='não',
                              variable=cate, value=0)
cate_neg_rb = ttk.Radiobutton(exames_f, text='negativo',
                              variable=cate, value=1)
cate_pos1_rb = ttk.Radiobutton(exames_f, text='< 50%',
                               variable=cate, value=2)
cate_pos2_rb = ttk.Radiobutton(exames_f, text='>= 50%',
                               variable=cate, value=3)

# Achados
achados_f = ttk.Labelframe(root, text='Achados:')
ec_l = ttk.Label(achados_f, text='EC: ')
ec_e = ttk.Entry(achados_f, textvariable=ec, width=5)
ec_nan_cb = ttk.Checkbutton(achados_f, text='NA', variable=ec_nan,
                            command=controle_ec)
sep4 = ttk.Separator(achados_f, orient=HORIZONTAL)
dominancia_l = ttk.Label(achados_f, text='Dominância: ')
dominancia_esq_rb = ttk.Radiobutton(achados_f, text='E',
                                    variable=dominancia, value=0)
dominancia_dir_rb = ttk.Radiobutton(achados_f, text='D',
                                    variable=dominancia, value=1)
dominancia_bal_rb = ttk.Radiobutton(achados_f, text='B',
                                    variable=dominancia, value=2)
tce_l = ttk.Label(achados_f, text='TCE: ')
tce_scale = Scale(achados_f, from_=0, to=5, resolution=1, orient=HORIZONTAL,
                  variable=tce)

da_l = ttk.Label(achados_f, text='DA: ')
dap_l = ttk.Label(achados_f, text='P', width=5, anchor=CENTER)
dam_l = ttk.Label(achados_f, text='M', width=5, anchor=CENTER)
dad_l = ttk.Label(achados_f, text='D', width=5, anchor=CENTER)
dap_b = ttk.Button(achados_f, textvariable=dap, command=lambda: trocar(dap),
                   width=4)
dap.set(0)
dam_b = ttk.Button(achados_f, textvariable=dam, command=lambda: trocar(dam),
                   width=4)
dam.set(0)
dad_b = ttk.Button(achados_f, textvariable=dad, command=lambda: trocar(dad),
                   width=4)
dad.set(0)

dg_l = ttk.Label(achados_f, text='DG: ')
dg_scale = Scale(achados_f, from_=0, to=5, resolution=1, orient=HORIZONTAL,
                 variable=dg)
ri_l = ttk.Label(achados_f, text='RI: ')
ri_scale = Scale(achados_f, from_=0, to=5, resolution=1, orient=HORIZONTAL,
                 variable=ri)
cx_l = ttk.Label(achados_f, text='CX: ')
cxp_l = ttk.Label(achados_f, text='P', width=8, anchor=CENTER)
cxd_l = ttk.Label(achados_f, text='D', width=8, anchor=CENTER)
cxp_b = ttk.Button(achados_f, textvariable=cxp, command=lambda: trocar(cxp),
                   width=7)
cxp.set(0)
cxd_b = ttk.Button(achados_f, textvariable=cxd, command=lambda: trocar(cxd),
                   width=7)
cxd.set(0)
mg_l = ttk.Label(achados_f, text='MG: ')
mg_scale = Scale(achados_f, from_=0, to=5, resolution=1, orient=HORIZONTAL,
                 variable=mg)
cd_l = ttk.Label(achados_f, text='CD: ')
cdp_l = ttk.Label(achados_f, text='P', width=5, anchor=CENTER)
cdm_l = ttk.Label(achados_f, text='M', width=5, anchor=CENTER)
cdd_l = ttk.Label(achados_f, text='D', width=5, anchor=CENTER)
cdp_b = ttk.Button(achados_f, textvariable=cdp, command=lambda: trocar(cdp),
                   width=4)
cdp.set(0)
cdm_b = ttk.Button(achados_f, textvariable=cdm, command=lambda: trocar(cdm),
                   width=4)
cdm.set(0)
cdd_b = ttk.Button(achados_f, textvariable=cdd, command=lambda: trocar(cdd),
                   width=4)
cdd.set(0)
dp_l = ttk.Label(achados_f, text='DP: ')
dp_scale = Scale(achados_f, from_=0, to=5, resolution=1, orient=HORIZONTAL,
                 variable=dp)
vp_l = ttk.Label(achados_f, text='VP: ')
vp_scale = Scale(achados_f, from_=0, to=5, resolution=1, orient=HORIZONTAL,
                 variable=vp)
achados_legenda = Message(
    achados_f, text='0) Sem placa\n1) < 25%\n2) 25-49%\n' +
    '3) 50-69%\n4) 70-99%\n5) Oclusão', justify=LEFT)

# Rodapé
obs_l = ttk.Label(text='Observações: ') 
obs_e = ttk.Entry(textvariable=obs, width=92)

laudado_l = ttk.Label(root, text='Laudado por: ')
laudado_combob = ttk.Combobox(root, textvariable=laudado_por, values=medicos,
                              width=8)

hj = date.today()
hoje = str(hj.day) + '/' + str(hj.month) + '/' + str(hj.year)
data.set(hoje)
data_l = ttk.Label(root, text='Data: ')
data_e = ttk.Entry(root, textvariable=data, width=10)

submeter_b = ttk.Button(root, text='Submeter', command=validar)
limpar_b = ttk.Button(root, text='Limpar', command=limpar_janela)

# Grid
dados_f.grid(row=2, column=0, padx=5, pady=5, sticky=N)
num_acesso_l.grid(row=3, column=0, sticky=W)
num_acesso_e.grid(row=3, column=1, sticky=W)
sep3.grid(row=4, column=0, columnspan=2, pady=5, sticky=W + E)
idade_l.grid(row=5, column=0, sticky=W)
idade_e.grid(row=5, column=1, sticky=W)
etnia_l.grid(row=6, column=0, sticky=W)
etnia_combob.grid(row=6, column=1, sticky=W)
peso_l.grid(row=7, column=0, sticky=W)
peso_e.grid(row=7, column=1, sticky=W)
altura_l.grid(row=8, column=0, sticky=W)
altura_e.grid(row=8, column=1, sticky=W)
sexo_l.grid(row=9, column=0, sticky=W)
sexo_m_rb.grid(row=9, column=1, sticky=E)
sexo_f_rb.grid(row=9, column=1, sticky=W)
sep6.grid(row=10, column=0, columnspan=2, pady=5, sticky=W + E)
origem_l.grid(row=11, column=0, columnspan=2, sticky=W)
origem_rb1.grid(row=12, column=0, columnspan=2, sticky=W)
origem_rb2.grid(row=13, column=0, columnspan=2, sticky=W)
sep7.grid(row=14, column=0, columnspan=2, pady=5, sticky=W + E)
indicacao_l.grid(row=15, column=0, columnspan=2, sticky=W)
indicacao_rb1.grid(row=16, column=0, columnspan=2, sticky=W)
indicacao_rb2.grid(row=17, column=0, columnspan=2, sticky=W)
indicacao_rb3.grid(row=18, column=0, columnspan=2, sticky=W)
indicacao_rb4.grid(row=19, column=0, columnspan=2, sticky=W)
indicacao_rb5.grid(row=20, column=0, columnspan=2, sticky=W)
indicacao_rb6.grid(row=21, column=0, columnspan=2, sticky=W)

antec_f.grid(row=2, column=1, padx=5, pady=5, sticky=N)
hf_dac_cb.grid(row=0, sticky=W, padx=10)
has_cb.grid(row=1, sticky=W, padx=10)
dlp_cb.grid(row=2, sticky=W, padx=10)
tbg_cb.grid(row=3, sticky=W, padx=10)
sedent_cb.grid(row=4, sticky=W, padx=10)
dm_cb.grid(row=5, sticky=W, padx=10)
iam_cb.grid(row=6, sticky=W, padx=10)
dac_cb.grid(row=7, sticky=W, padx=10)
equiv_dac_cb.grid(row=8, sticky=W, padx=10)
stent_cb.grid(row=9, sticky=W, padx=10)
rm_cb.grid(row=10, sticky=W, padx=10)
ic_cb.grid(row=11, sticky=W, padx=10)
fa_cb.grid(row=12, sticky=W, padx=10)
tpsv_cb.grid(row=13, sticky=W, padx=10)
a_vent_cb.grid(row=14, sticky=W, padx=10)

clinica_f.grid(row=2, column=2, padx=5, pady=5, sticky=N)
tipica_rb.grid(row=0, sticky=W)
p_anginosa_rb.grid(row=1, sticky=W)
p_n_anginosa_rb.grid(row=2, sticky=W)
equiv_anginoso_rb.grid(row=3, sticky=W)
assint_rb.grid(row=4, sticky=W)

medicamentos_f.grid(row=2, column=3, padx=5, pady=5, sticky=N)
bbloq_cb.grid(row=0, sticky=W)
iecabra_cb.grid(row=1, sticky=W)
bcc_cb.grid(row=2, sticky=W)
tiaz_cb.grid(row=4, sticky=W)
espirono_cb.grid(row=5, sticky=W)
furo_cb.grid(row=6, sticky=W)
nitrato_cb.grid(row=7, sticky=W)
hdz_cb.grid(row=8, sticky=W)
estatina_cb.grid(row=9, sticky=W)
aas_cb.grid(row=10, sticky=W)
p2y12_cb.grid(row=11, sticky=W)

exames_f.grid(row=2, column=4, padx=5, pady=5, sticky=N)
te_l.grid(row=0, sticky=W)
te_nao_rb.grid(row=1, sticky=W)
te_ineficaz_rb.grid(row=2, sticky=W)
te_neg_rb.grid(row=3, sticky=W)
te_pos_rb.grid(row=4, sticky=W)
sep1.grid(row=5, sticky=W + E)
cintilo_l.grid(row=6, sticky=W)
cintilo_nao_rb.grid(row=7, sticky=W)
cintilo_neg_rb.grid(row=8, sticky=W)
cintilo_pos1_rb.grid(row=9, sticky=W)
cintilo_pos2_rb.grid(row=10, sticky=W)
sep2.grid(row=11, sticky=W + E)
eco_l.grid(row=12, sticky=W)
eco_nao_rb.grid(row=13, sticky=W)
eco_neg_rb.grid(row=14, sticky=W)
eco_pos1_rb.grid(row=15, sticky=W)
eco_pos2_rb.grid(row=16, sticky=W)
sep5.grid(row=17, sticky=W + E)
cate_l.grid(row=18, sticky=W)
cate_nao_rb.grid(row=19, sticky=W)
cate_neg_rb.grid(row=20, sticky=W)
cate_pos1_rb.grid(row=21, sticky=W)
cate_pos2_rb.grid(row=22, sticky=W)

achados_f.grid(row=2, column=5, padx=5, pady=5, sticky=N)
ec_l.grid(row=0, column=0, sticky=W)
ec_e.grid(row=0, column=1, sticky=W)
ec_nan_cb.grid(row=0, column=1, sticky=E)
sep4.grid(row=1, columnspan=2, pady=5, sticky=W + E)
dominancia_l.grid(row=2, column=0, columnspan=2, sticky=W)
dominancia_esq_rb.grid(row=3, column=0, columnspan=2, sticky=W)
dominancia_dir_rb.grid(row=3, column=0, columnspan=2)
dominancia_bal_rb.grid(row=3, column=0, columnspan=2, sticky=E)
tce_l.grid(row=4, column=0, sticky=W + S)
tce_scale.grid(row=4, column=1, sticky=W)
dap_l.grid(row=5, column=1, sticky=W)
dam_l.grid(row=5, column=1)
dad_l.grid(row=5, column=1, sticky=E)
da_l.grid(row=6, column=0, sticky=W + S)
dap_b.grid(row=6, column=1, sticky=W)
dam_b.grid(row=6, column=1)
dad_b.grid(row=6, column=1, sticky=E)
dg_l.grid(row=7, column=0, sticky=W + S)
dg_scale.grid(row=7, column=1, sticky=W)
ri_l.grid(row=8, column=0, sticky=W + S)
ri_scale.grid(row=8, column=1, sticky=W)
cxp_l.grid(row=9, column=1, sticky=W)
cxd_l.grid(row=9, column=1, sticky=E)
cx_l.grid(row=10, column=0, sticky=W + S)
cxp_b.grid(row=10, column=1, sticky=W)
cxd_b.grid(row=10, column=1, sticky=E)
mg_l.grid(row=11, column=0, sticky=W + S)
mg_scale.grid(row=11, column=1, sticky=W)
cdp_l.grid(row=12, column=1, sticky=W)
cdm_l.grid(row=12, column=1)
cdd_l.grid(row=12, column=1, sticky=E)
cd_l.grid(row=13, column=0, sticky=W + S)
cdp_b.grid(row=13, column=1, sticky=W)
cdm_b.grid(row=13, column=1)
cdd_b.grid(row=13, column=1, sticky=E)
dp_l.grid(row=14, column=0, sticky=W + S)
dp_scale.grid(row=14, column=1, sticky=W)
vp_l.grid(row=15, column=0, sticky=W + S)
vp_scale.grid(row=15, column=1, sticky=W)
achados_legenda.grid(row=16, column=0, columnspan=2, pady=6, sticky=W)

obs_l.grid(row=13, column=0, sticky=E)
obs_e.grid(row=13, column=1, columnspan=4, sticky=W)
laudado_l.grid(row=14, column=0, sticky=E)
laudado_combob.grid(row=14, column=1, sticky=W)
data_l.grid(row=14, column=1, sticky=E)
data_e.grid(row=14, column=2, sticky=W)
submeter_b.grid(row=14, column=4, pady=10)
limpar_b.grid(row=14, column=3, pady=10)

root.mainloop()
