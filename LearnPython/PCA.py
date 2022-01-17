import numpy as np
from sklearn.decomposition import PCA

numbers = 4
dimension = 3
X_origin = np.random.rand(numbers, dimension)
X_new = X - np.mean(X_origin, axis=0)
varify = np.allclose(X_new.mean(axis=0), np.zeros(X_new.shape[1]))

C = np.matmul(X_new.T, X_new) / (X_new.shape[0] - 1)
eig_vals, eig_vecs = np.linalg.eig(C)
X_pca = np.matmul(X_new, eig_vecs)

U, S, Vh = np.linalg.svd(X_new, full_matrices=False, compute_uv=True)
varify = np.allclose(eig_vals, np.square(S) / (X_new.shape[0] - 1))
X_pca_svd = np.matmul(X_new, Vh.T)

pca = PCA(3)
X_pca_skl = pca.fit_transform(X)

print('origin')
print(X_new)

print('manual PCA')
print(X_pca)

print('SVD PCA')
print(X_pca_svd)

print('sklern PCA')
print(X_pca_skl)
