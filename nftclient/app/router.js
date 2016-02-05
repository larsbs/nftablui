import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('tables', { path: 'tables/:table_family' });
  this.route('table', { path: 'table/:table_id' });
  this.route('chain', { path: 'chain/:chain_id' });
  this.route('sets');
  this.route('dictionaries');
  this.route('files');
});

export default Router;
