<?php

namespace Modules\Admin\App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class AdminController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return view('admin::dashboard.dashboard');
    }

    public function crmDashboard()
    {
        return view('admin::dashboard.crm-dashboard');
    }

    public function accessRoles()
    {
        return view('admin::dashboard.app-access-roles');
    }

    public function accessPermission()
    {
        return view('admin::dashboard.app-access-permission');
    }

    public function userList()
    {
        return view('admin::dashboard.app-user-list');
    }

    public function userViewAccount()
    {
        return view('admin::dashboard.app-user-view-account');
    }

    public function userViewBilling()
    {
        return view('admin::dashboard.app-user-view-billing');
    }

    public function userViewConnections()
    {
        return view('admin::dashboard.app-user-view-connections');
    }

    public function userViewNotifications()
    {
        return view('admin::dashboard.app-user-view-notifications');
    }

    public function userViewSecurity()
    {
        return view('admin::dashboard.app-user-view-security');
    }

    public function invoiceList()
    {
        return view('admin::dashboard.app-invoice-list');
    }

    public function invoiceAdd()
    {
        return view('admin::dashboard.app-invoice-add');
    }

    public function invoiceEdit()
    {
        return view('admin::dashboard.app-invoice-edit');
    }

    public function invoicePreview()
    {
        return view('admin::dashboard.app-invoice-preview');
    }

    public function invoicePrint()
    {
        return view('admin::dashboard.app-invoice-print');
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        return view('admin::create');
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request) {}

    /**
     * Show the specified resource.
     */
    public function show($id)
    {
        return view('admin::show');
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit($id)
    {
        return view('admin::edit');
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, $id) {}

    /**
     * Remove the specified resource from storage.
     */
    public function destroy($id) {}
}
