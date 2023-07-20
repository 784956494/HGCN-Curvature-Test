# HGCN-Curvature-Test
I used the following command to generate a random graph with 5 nodes:
'''
graph_modeling generate random-tree --log_num_nodes 5
'''
I made sure that the graph generated is undirected by removing the "convert_to_outtree(t)" line in random_tree.py

Then I used convert.py to convert the npz file generted to a csv file. I noticed that the labels.npy file doesn't seem to be used in synthetic data link predictions, so I romoved it from training. I added a "random" option for load_data_lp to process the training date.

Then I run the following command to train (using curvature of 0.1 as an example): 
'''
python train.py --task lp --dataset random --model HGCN --lr 0.01 --dim 16 --num-layers 2 --num-layers 2 --act relu --bias 1 --dropout 0 --weight-decay 0 --manifold PoincareBall --normalize-feats 0 --log-freq --c -0.1
'''