import Ember from 'ember';

export default Ember.Controller.extend({
  chainTypes: ['filter', 'nat', 'route'],
  chainHooks: ['prerouting', 'input', 'forward', 'output', 'postrouting'],

  actions: {
    showAddChainModal: function () {
      this.get('addChainModal').send('show');
    },
    showEditModal: function () {
      this.get('editTableModal').send('show');
    },
    showEmptyConfirmationModal: function () {
      this.get('emptyConfirmationModal').send('show');
    },
    showDeleteConfirmationModal: function () {
      this.get('deleteConfirmationModal').send('show');
    },
    saveNewChain: function () {
      let chain = this.store.createRecord('chain', {
        name: this.get('newChainName'),
        type: this.get('newChainType'),
        hook: this.get('newChainHook'),
        priority: this.get('newChainPriority'),
        table: this.get('table')
      });
      chain.save()
        .then((model) => {
          // Reset values
          this.set('newChainName', '');
          this.set('newChainType', null);
          this.set('newChainHook', null);
          this.set('newChainPriority', '');
        })
        .catch((err) => {
          chain.deleteRecord();
          console.log(err.errors);
          Ember.$.notification('error', err.errors.message);
        });
    },
    emptyTable: function () {
      this.get('table.chains').toArray().forEach(x => x.destroyRecord());
    },
    deleteTable: function () {
      let table = this.get('table');
      let tableFamily = table.get('family');
      table.one('didDelete', () => this.transitionToRoute('tables', tableFamily));
      table.destroyRecord();
    }
  }
});
