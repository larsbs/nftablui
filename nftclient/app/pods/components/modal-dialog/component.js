import Ember from 'ember';

export default Ember.Component.extend({
  init: function () {
    this._super();
    this.get('parent').set(this.get('registerAs'), this);
  },

  actions: {
    okClicked: function () {
      this.$('.modal').modal('hide');
      this.sendAction('okListener');
    },
    show: function () {
      this.$('.modal').modal();
    }
  }
});
