module.exports = function(app) {
  var express = require('express');
  var tablesRouter = express.Router();

  var TABLES = [
    {
      id: 'ip:ip_lars',
      name: 'ip_lars',
      family: 'ip',
      chains: [
        'ip:ip_lars:filter_lars'
      ],
      sets: [
        'qwer'
      ],
      dictionaries: [
        'mydict'
      ]
    },
    {
      id: 'ip:ip2_lars',
      name: 'ip2_lars',
      family: 'ip',
      chains: []
    }
  ];

  tablesRouter.get('/', function(req, res) {
    res.send({
      'tables': TABLES
    });
  });

  tablesRouter.post('/', function(req, res) {
    res.status(201);
    var table = req.body.table;
    table.id = table.family + ':' + table.name;
    res.send({
      'table': table
    });
  });

  tablesRouter.get('/:id', function(req, res) {
    res.send({
      'table': TABLES.getById(req.params.id)
    });
  });

  tablesRouter.put('/:id', function(req, res) {
    res.send({
      'tables': {
        id: req.params.id
      }
    });
  });

  tablesRouter.delete('/:id', function(req, res) {
    res.status(204);
    res.send({});
  });

  app.use('/api/tables', tablesRouter);
};
