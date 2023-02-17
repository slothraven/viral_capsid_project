from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

import re
import time
import urllib

import database


def get_viper_id(browser, link):
    browser.get(link)
    time.sleep(5)
    pdb_id = re.findall(r'(?<=\=)(.*)(?=)', link)
    try:
        uniprot_id = browser.find_element(By.XPATH, f"//*[@id=\"Uni\"]/a").text
    except:
        uniprot_id = None
    host = browser.find_element(By.XPATH, f"//*[@id=\"Host\"]").text
    if host == "N/A":
        host = None
    method = browser.find_element(By.XPATH, f"//*[@id=\"Method\"]").text
    t_number = browser.find_element(By.XPATH, f"//*[@id=\"T_Number\"]").text
    if t_number == "N/A":
        t_number = None
    resolution = browser.find_element(By.XPATH, f"//*[@id=\"Reso\"]").text
    if resolution == "N/A" or resolution == "":
        resolution = None
    else:
        resolution = float(resolution)
    subunits = browser.find_element(By.XPATH, f"//*[@id=\"Num_Sub\"]").text
    if subunits == "N/A":
        subunits = None
    else:
        subunits = int(subunits)
    nsc = browser.find_element(By.XPATH, f"//*[@id=\"Net_Surf\"]").text
    sasa = browser.find_element(By.XPATH, f"//*[@id=\"Out_Sasa\"]").text
    radius_inner = re.findall(r'(?<=Inner:.)([0-9]*Å)(?=.)', browser.find_element(By.XPATH, f"//*[@id=\"Rad\"]").text)[
        0]
    radius_ave = re.findall(r'(?<=Ave:.)([0-9]*Å)(?=.)', browser.find_element(By.XPATH, f"//*[@id=\"Rad\"]").text)[0]
    radius_outer = re.findall(r'(?<=Outer:.)([0-9]*Å)(?=)', browser.find_element(By.XPATH, f"//*[@id=\"Rad\"]").text)[0]
    diameter_inner = \
    re.findall(r'(?<=Inner:.)([0-9]*Å)(?=.)', browser.find_element(By.XPATH, f"//*[@id=\"Diam\"]").text)[0]
    diameter_ave = re.findall(r'(?<=Ave:.)([0-9]*Å)(?=.)', browser.find_element(By.XPATH, f"//*[@id=\"Diam\"]").text)[0]
    diameter_outer = \
    re.findall(r'(?<=Outer:.)([0-9]*Å)(?=)', browser.find_element(By.XPATH, f"//*[@id=\"Diam\"]").text)[0]

    return {
        'pdb_id': pdb_id,
        'host': host,
        'method': method,
        't_number': t_number,
        'resolution': resolution,
        'subunits': subunits,
        'nsc': nsc,
        'sasa': sasa,
        'radius_inner': radius_inner,
        'radius_ave': radius_ave,
        'radius_outer': radius_outer,
        'diametr_inner': diameter_inner,
        'diametr_ave': diameter_ave,
        'diametr_outher': diameter_outer,
        'uniprot_id': uniprot_id
    }


def get_pdb_id(browser, link):
    pdb_id = re.findall(r'(?<=\=)(.*)(?=)', link)[0]
    browser.get(f'https://www.rcsb.org/structure/{pdb_id}')
    time.sleep(5)

    try:
        image_bottom_inf = browser.find_element(By.XPATH,
                                                f"//*[@id=\"Carousel-BiologicalUnit1\"]/div[4]").text.splitlines()
    except:
        return None
    global_stoichiometry = re.findall("(?<=Stoichiometry: )([^#]+)(?=)", image_bottom_inf[2])[0]
    global_summetry = re.findall(r'(?<=Symmetry: )([^#]+)(?=)', image_bottom_inf[1])[0]

    total_structure_weight = re.findall(r'(?<=: )([^#]+)(?= )',
                                        browser.find_element(By.XPATH, f"//*[@id=\"contentStructureWeight\"]").text)
    atom_count = \
    re.findall(r'(?<=: )([^#]+)(?= )', browser.find_element(By.XPATH, f"//*[@id=\"contentAtomSiteCount\"]").text)[
        0].replace(',', '.')
    modelled_residue_count = \
    re.findall(r'(?<=: )([^#]+)(?= )', browser.find_elements(By.XPATH, f"//*[@id=\"contentResidueCount\"]")[0].text)[0]
    deposited_residue_count = \
    re.findall(r'(?<=: )([^#]+)(?= )', browser.find_elements(By.XPATH, f"//*[@id=\"contentResidueCount\"]")[1].text)[0]
    unique_protein_chains = \
    re.findall(r'(?<=: )([^#]+)(?=)', browser.find_element(By.XPATH, f"//*[@id=\"contentProteinChainCount\"]").text)[0]
    try:
        doi_link = browser.find_element(By.XPATH, f"//*[@id=\"pubmedDOI\"]/a").get_attribute('href')
    except:
        doi_link = None
    image_link = browser.find_element(By.XPATH, f"//*[@id=\"Carousel-BiologicalUnit1\"]/img").get_attribute('src')
    urllib.request.urlretrieve(image_link, f"images/{pdb_id}.png")

    return {
        'global_stoichiometry': global_stoichiometry,
        'global_summetry': global_summetry,
        'total_structure_weight': total_structure_weight,
        'atom_count': float(atom_count),
        'modelled_residue_count': float(modelled_residue_count),
        'deposited_residue_count': float(deposited_residue_count),
        'unique_protein_chains': int(unique_protein_chains),
        'doi_link': doi_link,
        'image_path': f"images/{pdb_id}.png",
        'pdb_id': pdb_id
    }


def get_all_virus(browser):
    select = Select(browser.find_element(By.ID, 'Family_Combo'))
    n = 0
    url_list = []
    while True:
        n += 1
        try:
            select.select_by_value(str(n))
        except:
            break

        row = 1
        while True:
            try:
                url = browser.find_element(By.XPATH, f"//*[@id=\"table\"]/tr[{row}]/td[2]/div[2]/a").get_attribute(
                    "href")
                row += 1
                url_list.append(url)
            except:
                break
    return url_list


def update_data():
    option = Options()
    option.add_argument("--disable-infobars")
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"
    browser = webdriver.Chrome('chromedriver.exe', desired_capabilities=caps, options=option)
    browser.get('https://viperdb.org/Family_Index.php')
    time.sleep(15)
    url_links = get_all_virus(browser)
    for link in url_links:

        viper_dict = get_viper_id(browser, link)
        if database.check_pdb_id_viper(viper_dict['pdb_id'][0]):
            database.update_viper_data(viper_dict)
        else:
            print(viper_dict)
            database.create_viper_data(viper_dict)

        pdb_dict = get_pdb_id(browser, link)
        if database.check_pdb_id_pdb(pdb_dict['pdb_id'][0]):
            database.update_pdb_data(pdb_dict)
        else:
            database.create_pdb_data(pdb_dict)


update_data()