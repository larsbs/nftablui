import Ember from 'ember';

export default Ember.Controller.extend({
  selectedSet: null,

  actions: {
    showEditSetModal: function (set) {
      this.set('selectedSet', set);
      this.get('editSetModal').send('show');
    },
    editSet: function () {
      let set = this.get('selectedSet');
      set.set('items', set.get('itemsTextarea').split('\n').join(','));
      set.save();
    }
  }
});
