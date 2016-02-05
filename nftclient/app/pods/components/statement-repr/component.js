import Ember from 'ember';

export default Ember.Component.extend({
  tagName: 'tr',

  statementActionIsCounter: function () {
    return this.get('statement.action') === 'counter';
  }.property('statement'),
  statementActionIsJump: function () {
    return this.get('statement.action').startsWith('jump');
  }.property('statement'),
  statementActionIsDefault: function () {
    return this.get('statement.action') === 'counter';
  }.property('statement'),

  jumpActionChainName: function () {
    if (this.get('statementActionIsJump')) {
      return this.get('statement.action').split(' ')[1];
    }
  }.property('statement'),
  jumpActionChainId: function () {
    if (this.get('statementActionIsJump')) {
      return this.get('table.id') + ':' + this.get('statement.action').split(' ')[1];
    }
  }.property('statement'),
});
