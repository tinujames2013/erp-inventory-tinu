import { defineStore } from 'pinia';
import { api } from '../api';

export const useProductStore = defineStore('productStore', {
  state: () => ({
    products: []
  }),
  actions: {
    async fetchProducts() {
      const res = await api.get('products/');
      this.products = res.data;
    },
    async addProduct(product) {
      await api.post('products/', product);
      await this.fetchProducts();
    }
  }
});
