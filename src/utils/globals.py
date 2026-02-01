#Fonction permettant de choisir quel data frame utiliser
def choix_df(choix,global_df_brut,global_df_loisdeau,global_df_mean,global_meandf_repared,global_df_fusionnées,global_meandf_fusionnées,global_df_1,global_df_2,global_df_3,global_df_4,global_df_5,global_meandf_1,global_meandf_2,global_meandf_3,global_meandf_4,global_meandf_5):
    match choix:
        case 'DF_Brut':
            df = global_df_brut

        case 'df_mean':
            df = global_df_mean
        
        case 'meandf_repared':
            df = global_meandf_repared
        
        case 'df_fusionnées' :
            df = global_df_fusionnées
        
        case 'meandf_fusionnées':
            df = global_meandf_fusionnées
               
        case 'COP_loi_deau_df' if global_df_loisdeau:
            df = global_df_loisdeau
        
        case 'df_filtrees':
            df = global_df_filtrees
        
        case 'meandf_filtrees':
            df = global_meandf_filtrees

        case 'df_1':
            df=global_df_1

        case 'df_2':
            df=global_df_2

        case 'df_3':
            df=global_df_3

        case 'df_4':
            df=global_df_4

        case 'df_5':
            df=global_df_5

        case 'meandf_1':
            df=global_meandf_1

        case 'meandf_2':
            df=global_meandf_2

        case 'meandf_3':
            df=global_meandf_3

        case 'meandf_4':
            df=global_meandf_4

        case 'meandf_5':
            df=global_meandf_5

   
    #df = dd.DataFrame(df)
    #df = df.repartition(npartitions=desired_number_of_partitions)
    return df

dcc.Download(id="download"),
dcc.Download(id="download_F1_scission"),
dcc.Download(id="download_F2_scission"),

dcc.Download(id="download_df"),
