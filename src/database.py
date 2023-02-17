import sqlite3
import os.path


def update_viper_data(viper_dict):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()

    update_query = """
        update viper
        set 
            host = ?,
            method = ?,
            t_number = ?,
            resolution = ?,
            subunits = ?,
            nsc = ?,
            sasa = ?,
            radius_inner = ?,
            radius_ave = ?,
            radius_outer = ?,
            diametr_inner = ?,
            diametr_ave = ?,
            diametr_outher = ?
        where pdb = ?;
    """

    columns_values = (
        viper_dict['host'],
        viper_dict['method'],
        viper_dict['t_number'],
        viper_dict['resolution'],
        viper_dict['subunits'],
        viper_dict['nsc'],
        viper_dict['sasa'],
        viper_dict['radius_inner'],
        viper_dict['radius_ave'],
        viper_dict['radius_outer'],
        viper_dict['diametr_inner'],
        viper_dict['diametr_ave'],
        viper_dict['diametr_outher'],
        viper_dict['pdb_id'][0],
    )

    cursor.execute(update_query, columns_values)
    conn.commit()
    cursor.close()


def check_pdb_id_viper(pdb_id):
    conn = sqlite3.connect("database.sqlite3")
    cursor = conn.cursor()

    check_query = """select pdb from viper where pdb = ?"""
    cursor.execute(check_query, (pdb_id,))

    check_pdb_id = cursor.fetchall()

    if check_pdb_id == []:
        return False
    else:
        return True


def create_viper_data(viper_dict):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()

    insert_query = """
        insert into viper 
        (
            host,
            method,
            t_number,
            resolution,
            subunits,
            nsc,
            sasa,
            radius_inner,
            radius_ave,
            radius_outer,
            diametr_inner,
            diametr_ave,
            diametr_outher,
            pdb,
            uniprot_id
        ) 
        values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    columns_values = (
        viper_dict['host'],
        viper_dict['method'],
        viper_dict['t_number'],
        viper_dict['resolution'],
        viper_dict['subunits'],
        viper_dict['nsc'],
        viper_dict['sasa'],
        viper_dict['radius_inner'],
        viper_dict['radius_ave'],
        viper_dict['radius_outer'],
        viper_dict['diametr_inner'],
        viper_dict['diametr_ave'],
        viper_dict['diametr_outher'],
        viper_dict['pdb_id'][0],
        viper_dict['uniprot_id']
    )

    cursor.execute(insert_query, columns_values)
    conn.commit()
    cursor.close()


def update_pdb_data(pdb_dict):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()

    update_query = """
        update pdb
        set 
            global_stoichiometry = ?,
            global_summetry = ?,
            total_structure_weight = ?,
            atom_count = ?,
            modelled_residue_count = ?,
            deposited_residue_count = ?,
            unique_protein_chains = ?,
            doi_link = ?,
            image_path = ?,
            new_pdb_id = ?
        where pdb_id = ?;
    """

    columns_values = (
        pdb_dict['global_stoichiometry'],
        pdb_dict['global_summetry'],
        pdb_dict['total_structure_weight'],
        pdb_dict['atom_count'],
        pdb_dict['modelled_residue_count'],
        pdb_dict['deposited_residue_count'],
        pdb_dict['unique_protein_chains'],
        pdb_dict['doi_link'],
        pdb_dict['image_path'],
        pdb_dict['pdb_id'][0],
        pdb_dict['pdb_id'][0]
    )

    cursor.execute(update_query, columns_values)
    conn.commit()
    cursor.close()


def check_pdb_id_pdb(pdb_id):
    conn = sqlite3.connect("database.sqlite3")
    cursor = conn.cursor()

    check_query = """select pdb_id from pdb where pdb_id = ?"""
    cursor.execute(check_query, (pdb_id,))

    check_pdb_id = cursor.fetchall()

    if check_pdb_id == []:
        return False
    else:
        return True


def create_pdb_data(pdb_dict):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()

    insert_query = """
        insert into pdb 
        (
            pdb_id,
            global_stoichiometry,
            global_summetry,
            total_structure_weight,
            atom_count,
            modelled_residue_count,
            deposited_residue_count,
            unique_protein_chains,
            doi_link,
            image_path,
            new_pdb_id
        ) 
        values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    columns_values = (
        pdb_dict['pdb_id'][0],
        pdb_dict['global_stoichiometry'],
        pdb_dict['global_summetry'],
        pdb_dict['total_structure_weight'],
        pdb_dict['atom_count'],
        pdb_dict['modelled_residue_count'],
        pdb_dict['deposited_residue_count'],
        pdb_dict['unique_protein_chains'],
        pdb_dict['doi_link'],
        pdb_dict['image_path'],
        pdb_dict['pdb_id'][0]
    )

    cursor.execute(insert_query, columns_values)
    conn.commit()
    cursor.close()

# create_viper_data({'pdb_id': ['4v4m'], 'host': 'Plant', 'method': 'X-RAY DIFFRACTION', 't_number': '1', 'resolution': '1.45', 'subunits': '60', 'nsc': '+120 e- per virion', 'sasa': '4,763.4 Å² × 60', 'radius_inner': '45Å', 'radius_ave': '95Å', 'radius_outer': '97Å', 'diamert_inner': '90Å', 'diametr_ave': '190Å', 'diametr_outher': '194Å', 'uniprot_id': None})