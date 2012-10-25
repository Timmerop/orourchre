# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Card'
        db.create_table('deckocards_card', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rank', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('suit', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('deckocards', ['Card'])

    def backwards(self, orm):
        # Deleting model 'Card'
        db.delete_table('deckocards_card')

    models = {
        'deckocards.card': {
            'Meta': {'object_name': 'Card'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'suit': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['deckocards']