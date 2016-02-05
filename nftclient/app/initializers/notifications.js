import Ember from 'ember';

export default {
  name: 'notifications',
  initialize: function () {
    Ember.$.notification = function (type, text) {
      return noty({
        text: text,
        type: type,
        theme: 'relax',
        killer: true,
        layout: 'bottom'
      });
    }
  }
};
