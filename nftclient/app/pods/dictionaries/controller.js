import Ember from 'ember';

export default Ember.Controller.extend({
  selectedDictionary: null,
  actions: {
    showEditDictionaryModal: function (dictionary) {
      this.set('selectedDictionary', dictionary);
      this.get('editDictionaryModal').send('show');
    },
    editDictionary: function () {
      let dictionary = this.get('selectedDictionary');
      dictionary.set('items', dictionary.get('itemsTextarea').split('\n').join(','));
      dictionary.save();
    }
  }
});
