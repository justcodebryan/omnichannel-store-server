# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

route_stat = Blueprint('stat_page', __name__)


@route_stat.route('/index')
def index():
    return render_template('stat/index.html')


@route_stat.route('/product')
def product():
    return render_template('stat/product.html')


@route_stat.route('/member')
def member():
    return render_template('stat/member.html')


@route_stat.route('/share')
def share():
    return render_template('stat/share.html')
