import pandas as pd

class loadMasterData:
    def __init__(self,datasets_dir):
        item_dir = datasets_dir+"item_master.tsv"
        composite_dir = datasets_dir+"composite_master.tsv"
        ai_item_dir = datasets_dir+"AI_item_master.tsv"
        material_loss_dir = datasets_dir+"material_loss.tsv"
        shipping_cost_dir = datasets_dir+"輸送コスト.tsv"
        lc_cost_dir = datasets_dir+"LC間移動コスト.tsv"
        
        self.ai_item = pd.read_csv(ai_item_dir,sep="\t",skiprows=1,dtype=str)
        self.item_df = pd.read_csv(item_dir,sep="\t",skiprows=0,dtype=str)
        self.composite = pd.read_csv(composite_dir,sep="\t",skiprows=0,dtype=str)
        self.material_loss = pd.read_csv(material_loss_dir,sep="\t",skiprows=1,dtype=str)
        self.shipping_cost = pd.read_csv(shipping_cost_dir,sep="\t",skiprows=0,dtype=str)
        self.lc_cost = pd.read_csv(lc_cost_dir,sep="\t",skiprows=0,dtype=str)